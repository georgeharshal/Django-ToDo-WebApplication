from django.db import models

# Create your models here.
class TaskDB(models.Model):
    EmployeeName = models.CharField(max_length=100, null=True, blank=True)
    Task = models.CharField(max_length=100, null=True, blank=True)
    TaskDescription = models.TextField(max_length=100, null=True, blank=True)
    DeadLine = models.DateField(null=True, blank=True)
    Status = models.CharField(max_length=50, null=True, blank=True)

