# Register your models here.
from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'tech_required', 'language_needed')
    search_fields = ('project_name', 'tech_required', 'language_needed')
    filter_horizontal = ('assigned_to',)   # For clean multi-select UI

admin.site.register(Project, ProjectAdmin)
