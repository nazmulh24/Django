from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task


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
    # retrieving all tasks
    tasks = Task.objects.all()

    # retrieving a specific task by ID
    # task_2 = Task.objects.get(id=2)
    task_2 = Task.objects.get(pk=2)

    first_task = Task.objects.first()  # Get the first task

    context = {
        "tasks": tasks,
        "task_2": task_2,
        "first_task": first_task,
    }
    return render(request, "show_task.html", context)
