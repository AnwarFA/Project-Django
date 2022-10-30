"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import booking_event, create_events, get_home, register_user, signin_user, signout_user, get_events, get_event, create_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', get_home, name="home"),
    path("register/", register_user, name="register"),
    path("signin/", signin_user, name="signin"),
    path("signout/", signout_user, name="signout"),
    path("events/", get_events, name="event-list"),
    path("add/event/", create_events, name="create-events"),
    path("event/<int:event_id>/", get_event, name="event-details"),
    path("signup/", create_user, name="create-user"),
    path("booking/<int:booking_id>/", booking_event, name="booking-event")



]
