from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ApiAuthMixin:
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
