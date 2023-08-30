from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import authenticate
from django.forms import EmailField

from accounts.models import UserAccount


class RegistrationForm(UserCreationForm):
    email: EmailField = forms.EmailField(max_length=225,
                                         help_text="An email address is required. Please add a valid email address.")

    class Meta:
        model = UserAccount
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = UserAccount.objects.get(email=email)
        except UserAccount.DoesNotExist:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        try:
            account = UserAccount.objects.get(username=username)
        except UserAccount.DoesNotExist:
            return username
        raise forms.ValidationError(f'Username {username} is already in use.')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ('email', 'password')

    def clean_password(self):
        if self.is_valid():
            email = self.cleaned.data['email']
            password = self.cleaned.data['password']
            if not authenticate(email=email, password=password):  # if password is incorrect
                raise forms.ValidationError('Invalid Login')
