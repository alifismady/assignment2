from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    films_watched = models.TextField()
    films_title = models.TextField()
    films_rating = models.IntegerField()
    films_release_date = models.TextField()
    films_review = models.TextField()
