from django.db import models

# Create your models here.
from core.models import TimeStampedModel
from rooms.models import Room
from users.models import User


class Review(TimeStampedModel):
    """ Review model """
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.room}'
