from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from expenses_control.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "is_active", "is_staff", "is_superuser")

    search_fields = ("username", "email")

    list_filter = ("is_active", "is_staff", "is_superuser")

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("groups", "user_permissions", "is_active", "is_staff", "is_superuser")}),
        ("Timestamps", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {"fields": ("username", "email", "password1", "password2")}),
        ("Permissions", {"fields": ("groups", "user_permissions", "is_active", "is_staff", "is_superuser")}),
    )

    readonly_fields = ("last_login",)
