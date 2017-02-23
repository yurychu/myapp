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


class FormatSize(models.Model):
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()

    def __str__(self):
        return '{0} x {1}'.format(self.height, self.width)


class Book(models.Model):
    genre = models.ForeignKey(Genre)
    epos = models.ForeignKey(Epos, null=True, blank=True)
    tom = models.CharField(max_length=16, blank=True)

    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=128)
    publisher = models.ForeignKey(Publisher, null=True, blank=True)
    pub_year = models.PositiveIntegerField()
    number_of_pages = models.IntegerField()
    description = models.TextField()
    brief_content = models.TextField()
    cover = models.ImageField(blank=True, upload_to='book_covers')
    format_size = models.ForeignKey(FormatSize, null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    sold = models.BooleanField(default=False)  # отана / продана
    present = models.BooleanField(default=True)  # показывать в каталогах

    def __str__(self):
        return self.title
