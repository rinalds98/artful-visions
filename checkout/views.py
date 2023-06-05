from django.shortcuts import render


def checkout(request):
    """
    A view that returns the checkout page
    """
    return render(request, 'home/index.html')
