from django.shortcuts import render
from profiles.models import Testimonial


def index(request):
    """
    A view that returns the index page
    """
    testimonials = Testimonial.objects.filter(is_approved=True)

    context = {
        'testimonials': testimonials,
    }
    return render(request, 'home/index.html', context)
