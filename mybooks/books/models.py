from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Epos(models.Model):
    name = models.CharField(max_length=128)


class Book(models.Model):
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre)

    title = models.CharField(max_length=128)
    tom = models.CharField(max_length=16)
    pub_year = models.DateField()
    description = models.TextField()
    cover = models.ImageField()

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
