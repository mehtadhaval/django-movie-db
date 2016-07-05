from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class AuditMixin(object):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actor'


class PersonMovie(models.Model):
    person = models.ForeignKey(Person)
    movie = models.ForeignKey("Movie")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(AuditMixin, models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    total_time = models.IntegerField(help_text=_("Total movie runtime in minutes"), null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    director = models.ForeignKey(Person, related_name='movies_directed', null=True, blank=True)
    writer = models.ForeignKey(Person, related_name='movies_written', null=True, blank=True)
    actors = models.ManyToManyField(Person, through=PersonMovie, related_name='movies_acted')

    @property
    def genre(self):
        return ", ".join(self.genres.values_list("name", flat=True))

    def __str__(self):
        return self.title


class WatchList(AuditMixin, models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='watchlists')
    movies = models.ManyToManyField(Movie, related_name='watchlists')

    def __str__(self):
        return self.name