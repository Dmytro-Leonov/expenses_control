from knox.models import AuthToken

from expenses_control.users.models import User


def auth_knox_token_create(user: User) -> str:
    token = AuthToken.objects.create(user=user)[1]

    return token
