from urllib import request

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import authenticate
from django.forms import EmailField
from django.forms.utils import ErrorList
from accounts.models import UserAccount
from django.contrib.auth import get_user_model

UserAccount = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255,
                             help_text="An email address is required. Please add a valid email address.")

    class Meta:
        model = UserAccount
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = UserAccount.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        try:
            account = UserAccount.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username {username} is already in use.")


class AccountAuthenticationForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if not user or not user.is_active:  # if password is incorrect
                raise forms.ValidationError('Invalid Login')
            return self.cleaned_data
