from django.utils.translation import ugettext_lazy as _

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from user.models import Token


# Token认证
class TokenAuthentication(TokenAuthentication):
    # Authorization:Token 401f7ac837da42b97f613d789819ff93537bee6a
    keyword = 'Token'
    model = Token

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(access_token=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.user, token)

