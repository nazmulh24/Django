from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Max, Min, Sum, Avg


# --> Create your views here.
def home_view(request):
    # return render(request, "home.html")

    context = {
        "name": ["Shahriar", "Nazmul", "Hossain", "Shadhin"],
        "age": 22,
    }
    return render(request, "home.html", context)


def manager_dashboard(request):
    # tasks = Task.objects.all()
    tasks = Task.objects.select_related("details").prefetch_related("assigned_to").all()

    # total_task = tasks.count()  # --> Total Task
    # completed_task = Task.objects.filter(status="COMPLETED").count()  # --> Completed Task
    # in_progress_task = Task.objects.filter(status="IN_PROGRESS").count()  # --> In Progress Task
    # pending_task = Task.objects.filter(status="PENDING").count()  # --> Pending Task

    counts = Task.objects.aggregate(
        total_task=Count("id"),
        completed_task=Count("id", Q(status="COMPLETED")),
        in_progress_task=Count("id", Q(status="IN_PROGRESS")),
        pending_task=Count("id", Q(status="PENDING")),
    )

    context = {
        "tasks": tasks,
        "counts": counts,
        # "total_task": total_task,
        # "completed_task": completed_task,
        # "in_progress_task": in_progress_task,
        # "pending_task": pending_task,
    }
    return render(request, "Dashboard/manager-dashboard.html", context)


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
    # task_cnt = Task.objects.aggregate(num_task=Count("id"))

    # task_cnt = Project.objects.annotate(num_task=Count("task"))
    task_cnt = Project.objects.annotate(num_task=Count("task")).order_by("num_task")

    return render(request, "show_task.html", {"task_cnt": task_cnt})
