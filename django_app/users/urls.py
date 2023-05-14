from django.urls import path, include

from knox.views import LogoutView

from .views import UserLoginEmailPasswordLoginApi, UserGetMeApi


authentication_urlpatterns = [
    path("login-email-password/", UserLoginEmailPasswordLoginApi.as_view(), name="login-email-password"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

urlpatterns = [
    path("auth/", include((authentication_urlpatterns, "authentication"))),
    path("me/", UserGetMeApi.as_view(), name="user-get-me"),
]
