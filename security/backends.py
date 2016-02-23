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
            user = User.objects.get(email=email)

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