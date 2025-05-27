from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date
from django.db.models import Q


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
    """select_related(OneToOneField, ForeignKey) --> for single object"""

    # tasks = Task.objects.all() # --> N+1 Query Problem
    # tasks = Task.objects.select_related("details").all()  # --> Optimized Query
    # tasks = TaskDetail.objects.select_related("task").all()  # --> TaskDetail

    # tasks = Task.objects.select_related("project").all()

    """prefetch_related(Reverse_ForeignKey, ManyToManyField) --> for multiple objects"""

    # tasks = Project.objects.prefetch_related("task_set").all()
    
    # tasks = Task.objects.prefetch_related("assigned_to").all()
    tasks = Employee.objects.prefetch_related("task_set").all()

    return render(request, "show_task.html", {"tasks": tasks})
