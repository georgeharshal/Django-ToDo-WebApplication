from django.db import models


# Create your models here.
class EmployeeDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    EmailId = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)


class LoginDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    EmailId = models.CharField(max_length=100, null=True, blank=True)
    LastLogin = models.DateTimeField(null=True)