import uuid

from django.db import models
from maps.models import Event
import os

from people.helper import unique_slugify


# чтобы у всех файлов были оригинальные имена
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.directory_string_var, filename)


# таблица людей
class Person(models.Model):
    name = models.CharField(name='name', max_length=255)
    slug = models.SlugField(name='slug', db_index=True, unique=True)
    events = models.ManyToManyField(Event, name='events', blank=True)
    biography = models.TextField(name='biography', blank=True)
    photo = models.ImageField(name='photo',  upload_to='personalities')
    searchfield = models.TextField(name='searchfield', blank=True)

    class Meta:
        db_table = "person"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)
