from django.shortcuts import render, redirect
from profiles.models import Testimonial
from .models import Faq
from .forms import ContactForm, FaqSubmissionForm
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


def faq(request):
    """
    A view that returns the FAQ page
    """
    faqs = Faq.objects.filter(is_active=True)

    if request.method == 'POST':
        faq_form = FaqSubmissionForm(request.POST)
        if faq_form.is_valid():
            faq_form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('faq')
    else:
        faq_form = FaqSubmissionForm()

    context = {
        'faqs': faqs,
        'faq_form': faq_form,
    }
    return render(request, 'home/faq.html', context)
