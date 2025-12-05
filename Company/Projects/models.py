# Create your models here.
from django.db import models
from django.conf import settings
from Profile.models import ManagerProfile



class Project(models.Model):

    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='managed_projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    team_members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='assigned_projects')
    deadline = models.DateField()
    status = models.CharField(max_length=50, default="PENDING")  # PENDING / ONGOING / COMPLETED
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  



class Task(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")    
    title = models.CharField(max_length=200)     
    description = models.TextField()     
    status = models.CharField(max_length=20, default="Pending")    



class EmployeeUpdate(models.Model):

    Project = models.CharField()
    task = models.CharField()
    description = models.TextField()
    Things_To_Notice = models.TextField()
    Deadline = models.DateTimeField()


class InternUpdate(models.Model):

    Project = models.CharField()
    LearnToday = models.CharField()
    Source = models.CharField()
    WorkWith = models.TextField()

class NewjoineUpdate(models.Model):

    Announcement = models.CharField() 
    FieldToDecide = models.TextField()
    BePreparedFor = models.CharField()



class HrUpdate(models.Model):

    taskUpdate = models.TextField()
    NewRule = models.CharField()
    Notice = models.TextField()
    Celebration = models.TextField()
    Preparation = models.TextField()



   

