# Generated by Django 3.0.3 on 2020-02-11 17:03

from django.db import migrations

def seed(apps, schema_editor):
    Group = apps.get_model('todo', 'Group')
    Task = apps.get_model('todo', 'Task')
    
    monday = Group(group_name = "Monday")
    monday.save()
    tuesday = Group(group_name = "Tuesday")
    tuesday.save()
    wednesday = Group(group_name = "Wednesday")
    wednesday.save()

    Task(task_name = "Laundry", finished = False, notes = "Do by 4", group = monday).save()
    Task(task_name = "Dishes", finished = False, notes = "Do by 7", group = monday).save()
    Task(task_name = "Wash Car", finished = False, notes = "Car wash closes at 6", group = tuesday).save()
    Task(task_name = "Laundry", finished = False, notes = "I have a lot of clothes", group = wednesday).save()


def fallow(apps, schema_editor):
    Group = apps.get_model('todo', 'Group')
    Task = apps.get_model('todo', 'Task')
    Group.objects.all().delete()
    Task.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]