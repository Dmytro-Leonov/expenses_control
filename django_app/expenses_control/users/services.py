from typing import Optional

from expenses_control.users.models import User


def user_create(
    *,
    username: str,
    email: str,
    is_active: bool = True,
    is_staff: bool = False,
    is_superuser: bool = False,
    password: Optional[str] = None,
    last_login: Optional[str] = None,
) -> User:
    user = User.objects.create_user(
        username=username,
        email=email,
        is_active=is_active,
        is_staff=is_staff,
        is_superuser=is_superuser,
        password=password,
        last_login=last_login,
    )

    return user