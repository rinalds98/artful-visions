from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm, ProductForm, ProductSizeFormSet
from django.contrib.auth.decorators import login_required
import json
from decimal import Decimal


def all_products(request):
    """
    A view that shows all products
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))

            if sortkey == "category":
                sortkey = "category__name"

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!",
                )
                return redirect(reverse("products"))

            querie = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(querie)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    product_sizes = product.sizes.all()

    """
    code taken and adapted from
    https://bobbyhadz.com/blog/python-typeerror-object-of-type-decimal-is-not-json-serializable
    """
    sizes = []
    for product_size in product_sizes:
        sizes.append({"size": product_size.size, "price": product_size.price})

    sizes_json = json.dumps(sizes, cls=DecimalEncoder)

    # code taken and adapted from ^^^
    if request.method == "GET" and "product_size" in request.GET:
        selected_size = request.GET.get("product_size")
        product_size = product.sizes.filter(size=selected_size).first()

        if product_size:
            product_size.price = selected_size
            product_size.save()

    review_form = ReviewForm()

    if request.method == "POST":
        if request.user.is_authenticated:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                rating = review_form.cleaned_data["rating"]
                comment = review_form.cleaned_data["comment"]
                Review.objects.create(
                    product=product,
                    user=request.user,
                    rating=rating,
                    comment=comment,
                )
                return redirect("product_detail", product_id=product_id)
        else:
            messages.error(
                request,
                "Sorry, only registered users can do that.",
            )

    context = {
        "product": product,
        "reviews": reviews,
        "review_form": review_form,
        "sizes": sizes,
        "sizes_json": sizes_json,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        size_formset = ProductSizeFormSet(request.POST)

        if form.is_valid() and size_formset.is_valid():
            product = form.save()
            size_formset.instance = product
            size_formset.save()

            return redirect("product_detail", product_id=product.id)
    else:
        form = ProductForm()
        size_formset = ProductSizeFormSet()

    context = {
        "form": form,
        "size_formset": size_formset,
    }

    return render(request, "products/add_product.html", context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product_form = ProductForm(request.POST, instance=product)
        size_formset = ProductSizeFormSet(
            request.POST,
            prefix="size",
            instance=product,
        )

        if product_form.is_valid() and size_formset.is_valid():
            product = product_form.save()
            if product.has_sizes:
                size_formset.save()

            return redirect("product_detail", product_id=product.id)
    else:
        product_form = ProductForm(instance=product)
        size_formset = ProductSizeFormSet(prefix="size", instance=product)

    context = {
        "product": product,
        "product_form": product_form,
        "size_formset": size_formset,
    }

    return render(request, "products/edit_product.html", context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))
