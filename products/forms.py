from django import forms
from .models import Product, Category, Review, ProductSize
from django.forms import inlineformset_factory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "category",
            "sku",
            "name",
            "description",
            "price",
            "has_sizes",
            "image",
        ]


ProductSizeFormSet = inlineformset_factory(
    Product, ProductSize, fields=("size", "price"), extra=5, can_delete=False
)


class ProductSizeForm(forms.ModelForm):
    class Meta:
        model = ProductSize
        fields = ["size", "price"]


ProductSizeFormSet = inlineformset_factory(
    Product,
    ProductSize,
    form=ProductSizeForm,
    extra=5,
    can_delete=True,
)


STAR_CHOICES = (
    (5, ""),
    (4, ""),
    (3, ""),
    (2, ""),
    (1, ""),
)


class ReviewForm(forms.ModelForm):
    """
    This Class is responsible for creating the form on the review section
    of the homepage.
    """

    rating = forms.ChoiceField(
        choices=STAR_CHOICES,
        widget=forms.RadioSelect(
            attrs={
                "class": "icon",
                "aria-label": "star-rating",
            }
        ),
    )

    class Meta:
        model = Review
        fields = ["rating", "comment"]
