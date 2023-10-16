from django.db import models
from django.conf import settings
from django.db import models

from accounts.models import UserAccount


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
    likes = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(UserAccount, related_name='liked_posts', blank=True)


    def __str__(self):
        return str(self.content)

    def __repr__(self):
        return f"Post('{self.content}', '{self.createdAt}')"

class UserLike(models.Model):
    voter = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Changed from target_post
    is_liked = models.BooleanField(default=True)  # Changed from is_upvote

    class Meta:
        unique_together = ('voter', 'post')