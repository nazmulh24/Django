from django.shortcuts import render
from django.http import HttpResponse


# --> Create your views here.
def home_view(request):
    return render(request, "home.html")


def manager_dashboard(request):
    return render(request, "Dashboard/manager-dashboard.html")


def user_dashboard(request):
    return render(request, "Dashboard/user-dashboard.html")
