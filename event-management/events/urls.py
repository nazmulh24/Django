from django.contrib import admin
from django.urls import include, path
from events.views import (
    home_view,
    dashboard_view,
    event_view,
    category_view,
    participant_view,
    cEvent_view,
    eDetail_view,
)


urlpatterns = [
    path("home/", home_view, name="home"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("event/", event_view, name="event"),
    path("category/", category_view, name="category"),
    path("participant/", participant_view, name="participant"),
    path("create-event/", cEvent_view, name="cEvents"),
    path("event-details/", eDetail_view, name="eDetails"),
]
