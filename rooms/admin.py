from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from rooms.models import Room, RoomType, Amenity, Facility, HouseRule, Photo


@admin.register(RoomType, Amenity, Facility, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item admin """
    pass


# TabularInline
# StackedInline
class PhotoInline(admin.StackedInline):
    model = Photo


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room admin """
    inlines = [
        PhotoInline
    ]

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
        'count_amenities',
        'count_photos',
        'total_rating'
    ]

    raw_id_fields = ("host",)

    list_filter = ['city', 'instant_book', 'country', ]

    search_fields = ['country', 'city', ]

    filter_horizontal = ['amenity',
                         'facility',
                         'house_rules', ]

    def count_amenities(self, obj):
        return obj.amenity.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_amenities.short_description = 'Говеха'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo admin """

    list_display = ['__str__', 'get_thumbnail']

    def get_thumbnail(self, obj):
        return mark_safe(f"<img height='50px' src='{obj.file.url}'/>")

    get_thumbnail.short_description = 'Фото комнаты'
