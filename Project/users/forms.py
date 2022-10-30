from dataclasses import fields
from django import forms
from .models import Event
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "price", "description", "image", "category",
                  "organiser", "number_of_people", "date_of_event", "booking_status"]


User = get_user_model()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "password": forms.PasswordInput()
        }


class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class CreateUserForm(forms.Form):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "password": forms.PasswordInput()
        }
