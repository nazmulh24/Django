from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)

    # --> Many-to-One --> Many Events belong to One Category
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="events",
    )

    # --> Many-to-Many --> Many Participants can join Many Events
    participants = models.ManyToManyField(
        "Participant",
        related_name="events",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"


class Participant(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
