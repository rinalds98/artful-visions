from django.shortcuts import render, redirect
from profiles.models import Testimonial
from .forms import ContactForm
from django.contrib import messages


def index(request):
    """
    A view that returns the index page
    """
    testimonials = Testimonial.objects.filter(is_approved=True)

    context = {
        'testimonials': testimonials,
    }
    return render(request, 'home/index.html', context)


def about(request):
    """
    A view that returns the about page and
    renders the contact form
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        "form": form,
    }
    return render(request, 'home/about_me.html', context)
