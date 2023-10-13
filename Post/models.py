from django.db import models
from django.conf import settings
from django.db import models


# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    post_type = models.CharField(max_length=20, choices=[('picture', 'Picture'), ('video', 'Video')], default=None,
                                 null=True)
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True, default=None)
    video = models.FileField(upload_to='videos/', blank=True, null=True, default=None)
    updated = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def __repr__(self):
        return f"Post('{self.content}', '{self.createdAt}')"

# class Post (models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE
#     content = models.CharField(max_length=500)
#     post_picture = models.FileField(default="default.png", upload_to='post_picture')
#     post_video = models.FileField(default=None, upload_to='post_video', null=True, blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     createdAt = models.DateTimeField(auto_now_add=True)

# def __str__(self):
#     return  str(self.content)
#
# class Testimonial(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     content = models.CharField(max_length=100)
