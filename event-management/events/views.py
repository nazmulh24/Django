from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, "home.html")


def dashboard_view(request):
    return render(request, "dashboard.html")


def event_view(request):
    return render(request, "events.html")


def category_view(request):
    return render(request, "categories.html")


def participant_view(request):
    return render(request, "participants.html")
