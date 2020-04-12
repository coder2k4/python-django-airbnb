from django.db import models

# Create your models here.
from django.utils import timezone

from core.models import TimeStampedModel


class Reservation(TimeStampedModel):
    STATUS_CHOICES = [
        ("Pend", "Pending"),
        ("Conf", "Confirmed"),
        ("Cancld", "Canceled"),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=True)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", related_name="reservations", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name="reservations", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room} - {self.check_in}'

    def in_progress(self):
        now = timezone.now().date()
        return self.check_in <= now <= self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True
