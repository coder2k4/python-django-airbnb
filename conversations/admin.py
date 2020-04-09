from django.contrib import admin


# Register your models here.
from conversations.models import Message, Conversation


@admin.register(Message, Conversation)
class MessageAdmin(admin.ModelAdmin):
    pass
