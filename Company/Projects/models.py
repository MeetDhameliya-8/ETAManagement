# Create your models here.
from django.db import models
from django.conf import settings

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    tech_required = models.CharField(max_length=500)
    language_needed = models.CharField(max_length=200)

    # Employees + Interns assigned (Many-to-Many)
    assigned_to = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='assigned_projects'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
