from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)


class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = (
            "ADMIN",
            "Admin",
        )  # Como se guarde en la db, y como se muestra al usuario
        EMPLOYEE = "EMPLOYEE", "Employee"
        MANAGER = "MANAGER", "Manager"

    base_role = Role.EMPLOYEE

    role = models.CharField(
        max_length=50, choices=Role.choices
    )  # Se escoge lo definido en la class de arriba.

    # Sobreescribir el método save, set default role to user
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.role = self.base_role
    #         return super().save(*args, **kwargs)

    # If you are creating an employee profile the form will point to this model to create the user, that way, it already has the role selected as EMPLOYEE


##Kinda like a precreated filter, if you execute this method you will get all the user that have the role Employee.
class EmployeeManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.EMPLOYEE)


class ManagerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.MANAGER)


class Employee2(User):

    base_role: User.Role.EMPLOYEE

    employee = EmployeeManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for employees"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = (self.Role.EMPLOYEE)  # Assigning MANAGER role for Manager instances
        return super().save(*args, **kwargs)
    

#We will use a SIGNAL, something that let us know when an action is performed on a model. 
#In this case we will populate the user data on the EmployeeProfile table whenever a new "Employee" user is created

@receiver(post_save, sender=Employee2)
def create_user_profie(sender, instance, created, **kwargs):
    if created and instance.role == "EMPLOYEE":
        EmployeeProfile.objects.create(user=instance)

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Since we're using on_delete=models.CASCADE, whenever athe user related to this entry is eliminated the Profile table with update as well
    employee_id = models.IntegerField(null=True, blank=True)


class Manager(User):

    base_role: User.Role.MANAGER

    manager = ManagerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = (
                self.Role.MANAGER
            )  # Assigning MANAGER role for Manager instances
        return super().save(*args, **kwargs)

    def welcome(self):
        return "Only for managers"
    
class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Since we're using on_delete=models.CASCADE
    employee_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Manager)
def create_user_profie(sender, instance, created, **kwargs):
    if created and instance.role == "MANAGER":
        ManagerProfile.objects.create(user=instance)


