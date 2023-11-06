from django.contrib import admin

from people.models import Person


# Регистрация в админке
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}