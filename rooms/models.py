from django.db import models
from django_countries.fields import CountryField
from users.models import User
from core import models as core_models


class Room(core_models.TimeStampedModel):
    """ Определение модели ROOM, наследуемся от  TimeStampedModel"""

    name = models.CharField(max_length=150)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=90)
    price = models.IntegerField()
    address = models.CharField(max_length=150)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
