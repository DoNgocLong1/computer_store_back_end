from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

from computer_store.auth.exceptions import AuthenticationError, InvalidTokenError


class UserJWTAuthentication(JWTAuthentication):
    """
    Auth by JWT token or session ID for anonymous user
    """

    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except InvalidToken as e:  # Convert to standard exceptions
            raise InvalidTokenError(e.detail["detail"])
        except AuthenticationFailed as e:
            raise AuthenticationError(e.detail["detail"])
