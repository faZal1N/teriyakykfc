from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(name='first_name', max_length=255, blank=True)
    second_name = models.CharField(name='second_name', max_length=255, blank=True)
    phone_number = models.CharField(name='phone_number', max_length=18,
                                    error_messages={'unique': "Номер мобильного телефона уже существует"}, blank=False)
    editor_rights = models.BooleanField(name='editor_rights', default=False)
    email_verified = models.BooleanField(name='email_verified', default=False)

    class Meta:
        swappable = "AUTH_USER_MODEL"
        db_table = 'auth_user'
