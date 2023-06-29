from .models import DiscountCode
from django.http import JsonResponse


def discount_validation(request):
    if request.method == 'POST':
        discount_code = request.POST.get('discount_code')
        if discount_code:
            try:
                discount = DiscountCode.objects.get(code=discount_code)
                request.session['discount_code'] = discount_code
                # Discount code is valid
                context = {'valid': True}
            except DiscountCode.DoesNotExist:
                # Discount code is invalid
                context = {'valid': False}
        else:
            # Discount code not provided
            context = {'valid': False}
    else:
        # Invalid request method
        context = {'valid': False}

    return JsonResponse(context)
