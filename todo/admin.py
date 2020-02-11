from django.contrib import admin

# Register your models here.
from .models import Group, Task

admin.site.register([Group, Task])