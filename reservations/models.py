from django.db import models

# Create your models here.
from core.models import TimeStampedModel


class Reservation(TimeStampedModel):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Canceled", "Canceled"),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending"),
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room} - {self.check_in}'
