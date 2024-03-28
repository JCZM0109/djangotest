from django.contrib import admin
from .models import Department, Employee, User

# Register your models here.

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(User)
