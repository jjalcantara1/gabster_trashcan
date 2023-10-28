from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from django.utils import timezone


def is_token_expired(current_timestamp):
    now = timezone.localtime()
    return now > current_timestamp + timezone.timedelta(seconds=10)  # set to expire in 5 minutes


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                str(user.pk) + user.email + six.text_type(user.is_active) +
                six.text_type(timestamp)
        )


account_activation_token = AccountActivationTokenGenerator()
