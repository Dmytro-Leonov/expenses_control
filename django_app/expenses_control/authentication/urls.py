from django.urls import path

from knox.views import LogoutView

from expenses_control.authentication.apis import UserLoginEmailPasswordLoginApi

urlpatterns = [
    path("login-email-password/", UserLoginEmailPasswordLoginApi.as_view(), name="login-email-password"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
