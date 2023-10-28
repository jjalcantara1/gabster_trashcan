# forms.py
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'picture', 'video', 'post_type']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # Make the 'post_type' field not required
        self.fields['post_type'].required = False

    def clean(self):
        cleaned_data = super().clean()
        post_type = cleaned_data.get('post_type')
        content = cleaned_data.get('content')

        # If the post_type is 'picture', the content field is not required.
        if post_type == 'picture':
            if not content:
                # Set content to an empty string if not provided
                cleaned_data['content'] = ''
        return cleaned_data