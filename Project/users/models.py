from email.policy import default
from pyexpat import model
from unicodedata import category
from xml.etree.ElementInclude import default_loader
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Event(models.Model):
    class BookingStatus(models.TextChoices):
        booked = "yes, thank you!"
        not_booked = "no"
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(null=True)
    category = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Event")
    organiser = models.CharField(max_length=40, null=True)
    number_of_people = models.IntegerField(null=True)
    date_of_event = models.DateTimeField(null=True)
    booking_status = models.CharField(
        max_length=30, choices=BookingStatus.choices, null=True)


def __str__(self):
    return self.name
