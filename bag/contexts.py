from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from discounts.models import DiscountCode


def calculate_discounted_price(price, discount_percent):
    return price - (price * discount_percent / 100)


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    discount = 0
    bag = request.session.get('bag', {})
    discount_code = request.session.get('discount_code')

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            if product.has_sizes:
                product_size = product.sizes.first()
                price = product_size.price
            else:
                price = product.price
            total += item_data * price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'price': price,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                product_size = product.sizes.filter(size=size).first()
                price = product_size.price if product_size else None
                if price is not None:
                    total += quantity * price
                    product_count += quantity
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                        'price': price,
                    })

    if discount_code:
        try:
            discount = DiscountCode.objects.get(code=discount_code).discount
            grand_total = calculate_discounted_price(total, discount)
        except DiscountCode.DoesNotExist:
            discount = 0
            grand_total = total
    else:
        grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'grand_total': grand_total,
        'discount_code': discount_code,
    }

    return context
