from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Epos(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    genre = models.ForeignKey(Genre)
    epos = models.ForeignKey(Epos, null=True, blank=True)
    tom = models.CharField(max_length=16, blank=True)

    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=128)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)
    pub_year = models.PositiveIntegerField()
    description = models.TextField()
    brief_content = models.TextField()
    cover = models.ImageField(blank=True)

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
