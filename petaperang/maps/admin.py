from django.contrib import admin

from maps.models import Event, LocalMap
from people.models import Person


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(LocalMap)
class LocalMapAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
