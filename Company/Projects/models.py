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

    Project = models.CharField(max_length=255, blank=True, null=True)
    task = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    Things_To_Notice = models.TextField(blank=True, null=True)
    Deadline = models.DateTimeField(blank=True, null=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Project or "Employee Update"



class InternUpdate(models.Model):
    Project = models.CharField(max_length=255, blank=True, null=True)
    LearnToday = models.CharField(max_length=255, blank=True, null=True)
    Source = models.CharField(max_length=255, blank=True, null=True)
    WorkWith = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Project or "Intern Update"



class NewjoineUpdate(models.Model):


    Announcement = models.CharField(max_length=255, blank=True, null=True)

    FieldToDecide = models.TextField(blank=True, null=True)

    BePreparedFor = models.CharField(max_length=255, blank=True, null=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Announcement or "New Joinee Update"
    




class HrUpdate(models.Model):

    taskUpdate = models.TextField(blank=True, null=True)
    NewRule = models.CharField(max_length=255, blank=True, null=True)
    Notice = models.TextField(blank=True, null=True)
    Celebration = models.TextField(blank=True, null=True)
    Preparation = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.NewRule or "HR Update"


