from django.contrib.auth import get_user_model
from django.db.models import Q
from django.conf import settings

User = get_user_model()


class AuthenticationFailedException(Exception):
    pass


class CustomUserAuthBackend(object):
    """
    Custom authentication backend
    """

    def authenticate(self, email=None, password=None):
        if not email or not password:
            return None

        try:
            user = User.objects.get_pgp_annotated().select_related(
                'report_filer', 'report_filer_assistant', 'administrative_user',
                'administrative_user__account_type').get(Q(account_type=4) &
                                                         (Q(email__decrypted=email) |
                                                          Q(alternate_email__decrypted=email)))

            # verify password
            if user.check_password(password):
                return user
            else:
                raise AuthenticationFailedException(settings.GENERIC_ERROR)

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None