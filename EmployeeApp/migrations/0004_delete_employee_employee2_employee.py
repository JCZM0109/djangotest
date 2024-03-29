# Generated by Django 5.0.3 on 2024-03-28 00:26

import django.contrib.auth.models
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EmployeeApp", "0003_delete_employee_delete_student_employee"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Employee",
        ),
        migrations.CreateModel(
            name="Employee2",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("EmployeeApp.user",),
            managers=[
                ("employee", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("EmployeeId", models.AutoField(primary_key=True, serialize=False)),
                ("EmployeeName", models.CharField(max_length=500)),
                ("Department", models.CharField(max_length=500)),
                ("DateOfJoining", models.DateField()),
                ("PhotoFileName", models.CharField(max_length=500)),
            ],
        ),
    ]
