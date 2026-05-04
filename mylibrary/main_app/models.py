from django.db import models
from django.urls import reverse


STATUSES = (
    ('D', 'Didnt Start'),
    ('N', 'Not Finished'),
    ('F', 'Finished'),
)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-detail', kwargs={'pk': self.id})


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    year_published = models.IntegerField()
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'book_id': self.id})


class Status(models.Model):
    date = models.DateField('Status Date')
    status = models.CharField(max_length=1, choices=STATUSES, default=STATUSES[0][0])

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_status_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
