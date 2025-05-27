from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date


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
    # employees = Employee.objects.all()
    form = TaskModelForm()  # for GET

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():

            """For Model Form Data"""
            form.save()

            return render(
                request,
                "task_form.html",
                {"form": form, "message": "Task added successfully!!"},
            )

    context = {"form": form}
    return render(request, "task_form.html", context)


def view_task(request):
    tasks = Task.objects.filter(status="PENDING")

    # --> show tasks with due date today
    tasks2 = Task.objects.filter(due_date=date.today())

    # --> show tasks which priority is not LOW
    tasks3 = TaskDetail.objects.exclude(priority="L")

    context = {
        "tasks": tasks,
        "tasks2": tasks2,
        "tasks3": tasks3,
    }
    return render(request, "show_task.html", context)
