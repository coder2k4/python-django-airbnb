from django.contrib import admin

# Register your models here.
from conversations.models import Message, Conversation


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created')


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'count_messages')
    filter_horizontal = ['participants']
