from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    finished = models.BooleanField(default=False)
    notes = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='tasks')
    
    def __str__(self):
        return self.task_name