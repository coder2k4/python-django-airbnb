from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
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

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, default='Potato', max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    birthday = models.DateField(null=True, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10, null=True, blank=True)
    superhost = models.BooleanField(default=False)
