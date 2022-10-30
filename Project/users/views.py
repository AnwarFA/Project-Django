
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from users.forms import RegistrationForm, SigninForm
from users.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from .models import Event
from .forms import EventForm
from django.utils import timezone

# Create your views here.
User = get_user_model()


def get_home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def create_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return ("an 'invalid login' error message")
    form = CreateUserForm()
    context = {"form": form}
    return render(request, "create_user.html", context)


def register_user(req):
    form = RegistrationForm()
    if req.method == "POST":
        form = RegistrationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            if user is not None:
                login(req, user)
                return redirect("home")

    context = {"form": form}
    return render(req, "register.html", context)


def signout_user(req):
    logout(req)
    return redirect("home")


def signin_user(req):
    form = ()
    if req.method == "POST":
        form = SigninForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(req, auth_user)
                return redirect("home")

    context = {"form": form}
    return render(req, "signin.html", context)


def get_events(req):
    events = Event.objects.all()
    now = timezone.now()
    future_events = [e for e in events if e.date_of_event >= now]
    _events = []

    for event in events:

        _events.append(
            {
                "id": event.id,
                "name": event.name,
                "image": event.image,
                "organiser": event.organiser,
                "number_of_people": event.number_of_people,
                "date_of_event": event.date_of_event,
                "booking_status": event.booking_status,


            }
        )
    context = {"events": _events}
    return render(req, "event_list.html", context)


def create_events(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("event-list")

    context = {"form": form, }
    if request.user.is_anonymous:
        return redirect("signin")

    return render(request, "create_events.html", context)


def get_event(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        "event": {
            "id": event.id,
            "name": event.name,
            "image": event.image,
            "organiser": event.organiser,
            "number_of_people": event.number_of_people,
            "date_of_event": event.date_of_event,
            "booking_status": event.booking_status,

        }
    }
    return render(request, "event_details.html", context)


def booking_event(request, done_id):
    done = Event.objects.get(id=done_id)
    context = {
        "done": {
            "id": done.id,
            "name": done.name,
            "date_of_event": done.date_of_event,

        }


    }
    return render(request, "Booking_event.html", context)
