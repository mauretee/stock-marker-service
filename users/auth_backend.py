from django.contrib.auth.backends import ModelBackend
from users.models import CustomUser


class ApiKeyAuthBackend(ModelBackend):
    """
    Log in with api key.
    """
    def authenticate(self, api_key=None):
        try:
            return CustomUser.objects.get(api_key=api_key)
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, api_key):
        try:
            return CustomUser.objects.get(api_key=api_key)
        except CustomUser.DoesNotExist:
            return None
