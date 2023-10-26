import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )

    def is_token_expired(self, timestamp):
        # Check if the token has expired (10 minutes expiration time)
        expiration_time = timestamp + timezone.timedelta(minutes=10)
        return timezone.now() >= expiration_time


account_activation_token = AccountActivationTokenGenerator()
