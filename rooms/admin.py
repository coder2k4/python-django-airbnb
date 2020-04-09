from django.contrib import admin

# Register your models here.
from rooms.models import Room, RoomType, Amenity, Facility, HouseRule, Photo


@admin.register(RoomType, Amenity, Facility, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item admin """
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room admin """
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo admin """
    pass