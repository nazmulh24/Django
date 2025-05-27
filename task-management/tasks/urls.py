from django.urls import path
from tasks.views import (
    home_view,
    manager_dashboard,
    user_dashboard,
    create_task,
    view_task,
)


urlpatterns = [
    path("home/", home_view),
    path("manager-dashboard/", manager_dashboard),
    path("user-dashboard/", user_dashboard),
    path("create-task/", create_task),
    path("view-task/", view_task),
]
