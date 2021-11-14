from rest_framework import exceptions
from rest_framework import authentication
from rest_framework_api_key.models import APIKey
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate
from users.auth_backend import ApiKeyAuthBackend
from users.models import CustomUser


class ApiKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        if not 'Authorization' in request.headers:
            raise exceptions.AuthenticationFailed(_('No Authorization provided.'))
        api_key_name_key = request.headers['Authorization'].split()
        api_key_name = api_key_name_key[0]
        if not api_key_name=='Api-Key':
            raise exceptions.AuthenticationFailed(_('Bad api key header. It must be Api-key.'))
        if len(api_key_name_key) == 1:
            raise exceptions.AuthenticationFailed(_('No key provided.'))
        key = api_key_name_key[1]
        try:
            api_key = APIKey.objects.get_from_key(key)
        except APIKey.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Key provided is not valid.'))
        try:
            user = CustomUser.objects.get(api_key=api_key)
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('The user must be deleted or changed key.'))

        user = ApiKeyAuthBackend().authenticate(api_key=api_key)

        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (user, None)  # authentication successful
