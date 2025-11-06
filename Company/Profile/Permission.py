# requests/admin.py
from django.contrib import admin
from .models import HRRequest

class HRRequestAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'hr_user', 'status', 'reviewed_at')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Only HR, Manager, or superuser can see requests
        if request.user.is_hr or request.user.is_manager or request.user.is_superuser:
            return qs
        # Everyone else sees nothing
        return qs.none()

    def has_change_permission(self, request, obj=None):
        return request.user.is_hr or request.user.is_manager or request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_hr or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_hr or request.user.is_superuser

admin.site.register(HRRequest, HRRequestAdmin)
