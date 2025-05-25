from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
from tasks.models import Employee


# --> Create your views here.
def home_view(request):
    # return render(request, "home.html")

    context = {
        "name": ["Shahriar", "Nazmul", "Hossain", "Shadhin"],
        "age": 22,
    }
    return render(request, "home.html", context)


def manager_dashboard(request):
    return render(request, "Dashboard/manager-dashboard.html")


def user_dashboard(request):
    return render(request, "Dashboard/user-dashboard.html")


def create_task(request):
    # return render(request, "task_form.html")

    employees = Employee.objects.all()
    form = TaskForm(employees=employees)
    context = {"form": form}
    return render(request, "task_form.html", context)
