from django.db import models
from django.contrib import admin

class Employee(models.Model):
    eid = models.CharField(max_length=20,help_text="Employee")
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary=models.IntegerField()
    email=models.EmailField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('eid','name','age','salary','email')

