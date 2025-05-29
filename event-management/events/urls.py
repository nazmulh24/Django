from django.contrib import admin
from django.urls import include, path
from events.views import home_view


urlpatterns = [
    path("home/", home_view),
]
