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


    def get_readonly_fields(self, request, obj=None):
        user = request.user
        readonly_fields = self.readonly_fields

        if user.is_staff and not user.is_superuser:
            # staff member can't change sensitive fields
            readonly_fields += ("is_staff", "is_superuser", "groups", "user_permissions",)

            if not obj:
                return readonly_fields

            # staff member can't change other staff members
            if obj.is_staff and user != obj:
                readonly_fields += ("is_active", "username", "email",)

            # staff member can't deactivate himself
            if user == obj:
                readonly_fields += ("is_active",)

        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        user = request.user

        if not obj:
            return super().has_delete_permission(request, obj)

        # superuser can delete anyone
        if user.is_superuser:
            return True

        # staff member can't delete other staff members
        return not obj.is_staff
