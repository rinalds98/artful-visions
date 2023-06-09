from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm, TestimonialForm
from checkout.models import Order
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.',
                )
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    # Get testimonials for the current user
    if request.method == 'POST':
        testimonial_form = TestimonialForm(request.POST)
        if testimonial_form.is_valid():
            testimonial = testimonial_form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('profile')
    else:
        testimonial_form = TestimonialForm()

    template = 'profiles/profile.html'

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'testimonial_form': testimonial_form,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

