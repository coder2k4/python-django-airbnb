from django.db import models

# Create your models here.
from core.models import TimeStampedModel


class Conversation(TimeStampedModel):
    """ How this is fucking aggy :(( """
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="messages", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", related_name="messages", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says {self.message}"
