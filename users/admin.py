from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users.models import User


class AuthorAdmin(UserAdmin):
    """ Custom user admin """
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {
             "fields": ("avatar",
                        "gender",
                        "bio",
                        "birthday",
                        "language",
                        "currency",
                        "superhost",
                        )
        }),
    )

    # list_display = ('username', 'gender', 'language', 'currency', 'superhost')
    # list_filter = ('gender',)


admin.site.register(User, AuthorAdmin)
