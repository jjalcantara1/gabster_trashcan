from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm, AccountAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f'You are already authenticated as {user.email}.')
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # False since not yet verified
            user.save()

            # Send email verification link to the user
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            messages.success(request, "Please confirm your email address to complete the registration")
            return redirect('login')
        else:
            context['registration_form'] = form

    return render(request, 'accounts/register.html', context)


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True  # User will be active after successful activation
        user.is_email_verified = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can log in to your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request, *args, **kwargs):
    # form = AccountAutheticationForm(request.POST)
    context = {}

    user = request.user
    if user.is_authenticated:
        if user.is_email_verified:
            return redirect('pronfile_view')

    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        print(form.non_field_errors())
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user and user.is_email_verified:
                login(request, user)
                # destination = kwargs.get('next')
                if destination:
                    return redirect(destination)
                return redirect('profile', request.user.username)
                # return redirect('profile_view')
            else:
                form = AccountAuthenticationForm()

                context['login_form'] = form
    form = AccountAuthenticationForm(request.POST)
    return render(request, 'accounts/login.html', {'form': form})


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect


# def profile_view(request):
#     return redirect('profile')


def post(request):
    return render(request, "posts/post.html", {})


def testimonials(request):
    return render(request, "posts/testimonials.html", {})


def password_reset(request):
    return render(request, "accounts/password_reset.html", {})
