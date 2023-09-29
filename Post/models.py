from django.db import models
from django.conf import settings
from django.db import models


# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=15000)
    updated = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)


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
