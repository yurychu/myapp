from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=64)


class Genre(models.Model):
    name = models.CharField(max_length=64)


class Book(models.Model):
    title = models.CharField(max_length=128)
    publisher = models.ForeignKey(Publisher)
    genre = models.ForeignKey(Genre)
    pub_year = models.DateField()
    description = models.TextField()
    cover = models.ImageField()

