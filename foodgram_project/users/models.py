from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(
        'Адрес электронной почты',
        max_length=254,
        blank=False,
        unique=True,
        help_text='Введите адрес электронной почты',
    )

    username = models.CharField(
        'Username',
        max_length=150,
        unique=True,
        help_text='Введите имя пользователя',
    )

    first_name = models.CharField(
        'Имя',
        max_length=150,
        help_text='Введите ваше имя',

    )

    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        help_text='Введите вашу фамилию',

    )

    password = models.CharField(
        'Пароль',
        max_length=150,
        help_text='Введите пароль',
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]
