# Ex02 Django ORM Web Application
## Date: 23.11.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
...
admin.py

from django.contrib import admin
from .models import Employee,EmployeeAdmin
admin.site.register(Employee,EmployeeAdmin)

models.py

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


...


## OUTPUT
![web 3](https://github.com/user-attachments/assets/d032542d-068a-4c52-8f4a-8958f0d48da4)
![Screenshot 2024-12-14 101309](https://github.com/user-attachments/assets/95ce9006-338a-417a-884e-0018e996ae3e)

![Screenshot 2024-12-14 101245](https://github.com/user-attachments/assets/c277f85c-71bb-47c5-858d-15b1e3f33713)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
