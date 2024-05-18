from django.db import models
from django.utils import timezone

class Tasks(models.Model):
    created_at = models.DateTimeField()
    overdue = models.DateTimeField()
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    email = models.EmailField()

class OverdueTasks(models.Model):
    created_at = models.DateTimeField()
    overdue = models.DateTimeField()
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    email = models.EmailField()
