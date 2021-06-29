from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    """Регистрация пользователя в админке с полем role"""
    list_display = ('role',)


admin.site.register(User, UserAdmin)
