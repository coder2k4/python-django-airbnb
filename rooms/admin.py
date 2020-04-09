from django.contrib import admin

# Register your models here.
from rooms.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass
