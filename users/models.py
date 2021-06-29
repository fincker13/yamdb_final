from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoles(models.TextChoices):
    """Роли пользователей"""
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class User(AbstractUser):
    email = models.EmailField(verbose_name='email адрес',
                              unique=True)
    role = models.CharField(verbose_name='Роль пользователя',
                            max_length=9,
                            choices=UserRoles.choices,
                            default=UserRoles.USER)
    bio = models.TextField(verbose_name='Информация о себе',
                           blank=True)

    class Meta:
        ordering = ('-id',)

    @property
    def is_admin(self):
        return (self.is_staff
                or self.role == UserRoles.ADMIN
                or self.is_superuser)

    @property
    def is_moderator(self):
        return self.role == UserRoles.MODERATOR
