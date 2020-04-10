from django.db import models
from django_countries.fields import CountryField
from users.models import User
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):
    """ Абстрактный класс, добавляюшщий поле name """
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ RoomType """
    ordering = ['-created']
    pass


class Amenity(AbstractItem):
    """ Amenity """
    pass

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ Facility """
    pass


class HouseRule(AbstractItem):
    """ HouseRule """
    pass


class Photo(AbstractItem):
    """ Photo """
    caption = models.CharField(max_length=90)
    file = models.ImageField()
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


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
    host = models.ForeignKey(User, related_name="rooms", on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True)
    amenity = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facility = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings/len(all_reviews)
