from django.contrib import admin

# Register your models here.
from reservations.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """ ReservationAdmin """
    list_display = ('room', 'status', 'check_in', 'check_out', 'in_progress', 'is_finished')
