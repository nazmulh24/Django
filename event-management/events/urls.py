from django.contrib import admin
from django.urls import include, path
from events.views import (
    home_view,
    dashboard_view,
    event_view,
    category_view,
    participant_view,
)


urlpatterns = [
    path("home/", home_view),
    path("dashboard/", dashboard_view),
    path("event/", event_view),
    path("category/", category_view),
    path("participant/", participant_view),
]
