from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager    # AbstractBaseUser - user creation
                                                                            # BaseUserManager- managing users


# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Please input an email address")
        if not username:
            raise ValueError("Please input a username")

        user = self.model(
            email-self.normalize_email(email), # normalize email can only be called in BaseUserManager
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    ''' # implement ba natin?
    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email-self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
            '''


class UserAccount(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=50, unique=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now='True')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email', 'first_name']

    objects = UserAccountManager()

    # shows what to be displayed when creating user object
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return


