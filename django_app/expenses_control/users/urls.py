from django.urls import path

from expenses_control.users.apis import UserGetMeApi

urlpatterns = [
    path("me/", UserGetMeApi.as_view(), name="user-get-me"),
]
