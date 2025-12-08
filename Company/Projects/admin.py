# Register your models here.
from django.contrib import admin
from .models import Project, Task,EmployeeUpdate, InternUpdate, NewjoineUpdate, HrUpdate
from django.core.exceptions import PermissionDenied




@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'manager', 'deadline', 'status', 'created_at')
    list_filter = ('status', 'deadline', 'manager')
    search_fields = ('title', 'manager__email')




@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status')
    list_filter = ('status', 'project')
    search_fields = ('title', 'project__title')







  











   

@admin.register(EmployeeUpdate)
class EmployeeUpdateAdmin(admin.ModelAdmin):
    list_display = ("Project", "task", "Deadline")
    search_fields = ("Project", "task", "description", "Things_To_Notice")
    list_filter = ("Deadline",)
    ordering = ("-Deadline",)


@admin.register(InternUpdate)
class InternUpdateAdmin(admin.ModelAdmin):
    list_display = ("Project", "LearnToday", "Source")
    search_fields = ("Project", "LearnToday", "Source", "WorkWith")
    ordering = ("Project",)


@admin.register(NewjoineUpdate)
class NewjoineUpdateAdmin(admin.ModelAdmin):
    list_display = ("Announcement", "BePreparedFor")
    search_fields = ("Announcement", "BePreparedFor", "FieldToDecide")
    ordering = ("Announcement",)


@admin.register(HrUpdate)
class HrUpdateAdmin(admin.ModelAdmin):
    list_display = ("NewRule", "taskUpdate", "Notice")
    search_fields = ("NewRule", "taskUpdate", "Notice", "Celebration", "Preparation")
    ordering = ("NewRule",)
    


