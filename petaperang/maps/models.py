from django.db import models

from people.helper import unique_slugify


class Event(models.Model):
    name = models.CharField(name='name', max_length=255)
    slug = models.SlugField(name='slug', db_index=True, unique=True)
    begin = models.DateField(name='begin')
    end = models.DateField(name='end')
    description = models.TextField(name='description')
    x = models.FloatField(name='x')
    y = models.FloatField(name='y')
    searchfield = models.TextField(name='searchfield', blank=True)
    zoom = models.IntegerField(name='zoom', blank=True, default=11)
    kml = models.URLField(name='kml', blank=True)

    class Meta:
        db_table = 'event'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class LocalMap(models.Model):
    name = models.CharField(name='name', max_length=255)
    slug = models.SlugField(name='slug', db_index=True, unique=True)
    description = models.TextField(name='description')
    small_map = models.ImageField(name='small_map')
    event_link = models.ForeignKey(Event, on_delete=models.CASCADE)
    url = models.URLField(name='url', blank=True)
    x = models.FloatField(name='x')
    y = models.FloatField(name='y')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)
