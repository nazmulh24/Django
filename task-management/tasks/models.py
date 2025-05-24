from django.db import models

# ---> Create your models here.
""" 
class Example(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
"""


class Task(models.Model):
    # --> Error skip korar jonno project k comment kore dilam
    # project = models.ForeignKey(
    #     "Project",
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    # )  # ------------------------> Many-to-One

    # --> then shell a kaj korar por...
    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        default=1,
    )  # -------------------------> Many-to-One

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# -----> Relations : a)--> One-to-One   ||  b)--> Many-to-One   ||  c)--> Many-to-Many


# --> One-to-One
class TaskDetail(models.Model):
    HIGH = "H"
    MEDIUM = "M"
    LOW = "L"

    PRIORITY_OPTIONS = (
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    )

    task = models.OneToOneField(Task, on_delete=models.CASCADE)  # --> One-to-One

    assign_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)

    """ 
    --> Task.objects.get(id=1)
    
    select *
    from Task
    where id = 1;
    
    ----- ORM -----
    """


# --> Many-to-One
class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()


# --> Many-to-Many
