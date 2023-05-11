from django.urls import path

from knox.views import LogoutView

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
]
