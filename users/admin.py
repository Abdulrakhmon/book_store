from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone']
    search_fields = ['email', 'first_name', 'last_name', 'phone']

