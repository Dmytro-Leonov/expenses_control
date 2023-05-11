from django.urls import path, include

urlpatterns = [
    path("auth/", include(("expenses_control.authentication.urls", "authentication"))),
    path("users/", include(("expenses_control.users.urls", "users"))),
]
