from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("events/", include("events.urls")),  # ---> Include __ events app __ urls
] + debug_toolbar_urls()
