from .models import DiscountCode
from django.http import JsonResponse


def discount_validation(request):
    if request.method == 'POST':
        discount_code = request.POST.get('discount_code')
        if discount_code:
            try:
                discount = DiscountCode.objects.get(code=discount_code)
                context = {'valid': True}
            except DiscountCode.DoesNotExist:
                context = {'valid': False}
        else:
            context = {'valid': False}
    else:
        context = {'valid': False}

    return JsonResponse(context)
