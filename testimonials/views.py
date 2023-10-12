from django.db.models import Avg
from django.urls import reverse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TestimonialForm
from accounts.models import UserAccount
from django.contrib.auth.decorators import login_required

@login_required
def add_testimonial(request, user_to_username):
    user_to = get_object_or_404(UserAccount, username=user_to_username)

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user_from = request.user
            testimonial.user_to = user_to
            testimonial.save()
            print("Testimonial saved successfully")
            form.cleaned_data['content'] = ""
            # form.cleaned_data['rating'] = None  # Clear the rating field

            return redirect(reverse('view_testimonials', kwargs={'user_to_username': user_to_username}))
        else:
            print("Form errors:", form.errors)
    else:
        form = TestimonialForm(initial={'user_to': user_to})

    return render(request, 'posts/testimonials.html', {'form': form})


def view_testimonials(request, user_to_username):
    # Debug print to check if user_to_username is correct
    print("user_to_username:", user_to_username)

    user = get_object_or_404(UserAccount, username=user_to_username)
    # Debug print to check if the correct user is retrieved
    print("User retrieved:", user)

    # Check if the logged-in user is viewing their own profile or another user's profile
    if user == request.user:
        # If the user is viewing their own profile
        testimonials_received = Testimonial.objects.filter(user_to=user).order_by('-createdAt')
    else:
        # If the user is viewing another user's profile
        testimonials_received = Testimonial.objects.filter(user_to=user).order_by('-createdAt')

    return render(request, 'testimonial/view_testimonial.html', {
        'user': user,
        'testimonials_received': testimonials_received,
    })

@login_required
def testimonial_detail(request, user_to_username, testimonial_id):
    user = get_object_or_404(UserAccount, username=user_to_username)
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id, user_to=user)
    return render(request, 'testimonial/testimonial_detail.html', {'testimonial': testimonial})
