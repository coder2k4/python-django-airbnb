from django.contrib import admin

# Register your models here.
from lists.models import List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'count_rooms',)
    search_fields = ('name',)
    filter_horizontal = ('rooms',)
