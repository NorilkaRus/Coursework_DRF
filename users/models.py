from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
# Create your models here.
NULLABLE = {'blank':  True, 'null': True}


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Необходим e-mail")
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        email = GlobalUserModel.normalize_username(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='E-mail')
    telegram = models.CharField(max_length=50, unique=True, verbose_name='Telegram', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', **NULLABLE)
    is_active = models.BooleanField(verbose_name='Активность', default=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
