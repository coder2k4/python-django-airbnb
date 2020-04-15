import uuid

from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags

from config import settings


class User(AbstractUser):
    """ Custom user model """

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Potato', 'Potato'),
    ]

    LANGUAGE_CHOICES = [
        ('En', 'English'),
        ('Ru', 'Russian'),
        ('Pot', 'Potato'),
    ]

    CURRENCY_CHOICES = [
        ('Usd', 'Dollar'),
        ('Rub', 'Ruble'),
        ('Chips', 'Chips'),
    ]

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, default='Potato', max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthday = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, blank=True, default='Ru')
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10, blank=True, default='Rub')
    superhost = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def verify_email(self):
        if self.email_confirmed is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string('emails/verify_email.html', {'secret': secret})
            send_mail("Verify YOUR Account"
                      , strip_tags(html_message)
                      , settings.EMAIL_FROM
                      , [self.email]
                      , fail_silently=True
                      , html_message=html_message)
            self.save()
