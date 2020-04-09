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
    list_display = [
        'name',
        'country',
        'city',
        'price',
        'guests',
        'beds',
        'bedrooms',
        'baths',
        'check_in',
        'check_out',
        'instant_book',
        'count_amenities'
    ]

    list_filter = ['city', 'instant_book', 'country', ]

    search_fields = ['country', 'city', ]

    filter_horizontal = ['amenity',
                         'facility',
                         'house_rules',]

    def count_amenities(self, obj):
        return obj.amenity.count()

    count_amenities.short_description = 'Говеха'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo admin """
    pass
