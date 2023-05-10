from django.contrib import admin

from expenses_control.users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass