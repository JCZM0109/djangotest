# Generated by Django 5.0.3 on 2024-03-28 00:25

import django.contrib.auth.models
import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("EmployeeApp", "0002_student"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Employee",
        ),
        migrations.DeleteModel(
            name="Student",
        ),
        migrations.CreateModel(
            name="Employee",
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
    ]