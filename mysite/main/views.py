from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Events
from .forms import CreateEvent


def index(response, id):
    e = Events.objects.get(id=id)
    print(f'Event: {e.name}, date: {e.date}')
    return render(response, "main/index.html", {"e": e})


def home(response):
    return render(response, "main/home.html")


def create_event(response):
    if response.method == 'POST':
        form = CreateEvent(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            date = form.cleaned_data["date"]
            print(f'Date = {date}')
            e = Events(name=name, date=date)
            e.save()
            response.user.events.add(e)
        return HttpResponseRedirect(f"/index/{e.id}")
    else:
        form = CreateEvent()
        return render(response, "main/create.html", {"form": form})
