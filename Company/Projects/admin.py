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







  















class ManagerOnlyAdminMixin:


    def _is_manager(self, request):
        return bool(request.user and request.user.is_active and hasattr(request.user, 'manager_profile'))

    def has_add_permission(self, request):

        if request.user.is_superuser:
            return True
        return self._is_manager(request)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        
        if not self._is_manager(request):
            return False
        
        if obj is not None and hasattr(obj, 'manager'):
            return obj.manager == request.user
        return True

    def has_change_permission(self, request, obj=None):
    
        if request.user.is_superuser:
            return True
        
        if not self._is_manager(request):
            return False
        
        if obj is not None and hasattr(obj, 'manager'):
            return obj.manager == request.user
        return True

   

@admin.register(EmployeeUpdate)
class EmployeeUpdateAdmin(ManagerOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('Project', 'task', 'created_by', 'created_at')
    search_fields = ('Project', 'task', 'created_by__email')



@admin.register(InternUpdate)
class InternUpdateAdmin(ManagerOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('Project', 'LearnToday', 'created_by', 'created_at')
    search_fields = ('Project', 'LearnToday')



@admin.register(NewjoineUpdate)
class NewjoineUpdateAdmin(ManagerOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('Announcement', 'created_by', 'created_at')
    search_fields = ('Announcement',)



@admin.register(HrUpdate)
class HrUpdateAdmin(ManagerOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('NewRule', 'created_by', 'created_at')
    search_fields = ('NewRule', 'Notice')
    


