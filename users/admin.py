from django.contrib import admin

# Register your models here.
from users.models import User


class AuthorAdmin(admin.ModelAdmin):
    """ Custom user admin """

    list_display = ('username', 'gender', 'language', 'currency', 'superhost')
    list_filter = ('gender',)


admin.site.register(User, AuthorAdmin)
