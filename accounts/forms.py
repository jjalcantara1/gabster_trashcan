from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
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


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ('email', 'password')

    def __init__(
            self,
            data=None,
            files=None,
            auto_id="id_%s",
            prefix=None,
            initial=None,
            error_class=ErrorList,
            label_suffix=None,
            empty_permitted=False,
            instance=None,
            use_required_attribute=None,
            renderer=None,
    ):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        self.cleaned = None

    def clean_password(self):
        if self.is_valid():
            email = self.cleaned.data['email']
            password = self.cleaned.data['password']
            if not authenticate(email=email, password=password):  # if password is incorrect
                raise forms.ValidationError('Invalid Login')
