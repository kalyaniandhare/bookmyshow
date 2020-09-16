from django.contrib.postgres.fields import ArrayField
from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager,
                     self).get_queryset().all()


class Movie(models.Model):
    objects = ActiveManager()

    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, verbose_name="Select genre",
                             null=True, blank=True)
    director = models.CharField(max_length=255)
    imdb_score = models.CharField(max_length=10, null=True)
    popularity = models.CharField(max_length=10, null=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name
