from django.contrib import admin

from people.models import Person


# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}