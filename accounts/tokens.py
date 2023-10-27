from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from django.utils import timezone


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                str(user.pk) + user.email + six.text_type(user.is_active) +
                six.text_type(timestamp)
        )

    def is_token_expired(self, timestamp):
        now = timezone.now()
        return now > timestamp + timezone.timedelta(minutes=1)


account_activation_token = AccountActivationTokenGenerator()
