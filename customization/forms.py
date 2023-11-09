from django import forms
from accounts.models import UserAccount

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = [
            'profile_image',
            'profile_cover',
            'profile_song',
            'profile_background',
            'hide_email',
            'bio',
            'location',
            'color',
            'backgroundColor',
            'font_preference',
        ]
