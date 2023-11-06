from django.contrib import admin

from home.models import User

# Register your models here.
# Регистрация бд в админке
admin.site.register(User)