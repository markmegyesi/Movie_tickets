from django.db import models

class MovieModel(models.Model):
    movie_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    ticket_left = models.PositiveIntegerField()
    room_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'movies'

    def __str__(self):
        return(f"{self.movie_name}")
