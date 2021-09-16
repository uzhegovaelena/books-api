from django.db import models



class Book(models.Model):
    class Rating(models.TextChoices):
        great = '5'
        good = '4'
        normal = '3'
        bad = '2'
        very_bad = '1'

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    favorites = models.BooleanField(default=False)
    review = models.TextField(blank=True)
    rating = models.CharField(max_length=255, choices=Rating.choices, default=Rating.great)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
