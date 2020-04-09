from django.contrib import admin

# Register your models here.
from lists.models import List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    pass