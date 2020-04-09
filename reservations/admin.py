from django.contrib import admin

# Register your models here.
from reservations.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """ ReservationAdmin """
    pass
