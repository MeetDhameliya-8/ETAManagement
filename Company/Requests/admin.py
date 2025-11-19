# requests/admin.py
'''from django.contrib import admin
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

admin.site.register(HRRequest, HRRequestAdmin)'''


from django.contrib import admin
from .models import HRRequest
from Profile.models import NewJoineProfile  # import your profile model


class HRRequestAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'hr_user', 'status', 'reviewed_at')

    # -------------------------------
    # CREATE PROFILE ON APPROVAL
    # -------------------------------
    def save_model(self, request, obj, form, change):
        old_status = None

        if obj.pk:
            old_status = HRRequest.objects.get(pk=obj.pk).status

        super().save_model(request, obj, form, change)

        # If HR changes status from "Pending" to "Approved"
        if old_status != 'Approved' and obj.status == 'Approved':
            # Create NewJoineeProfile only if not already created
            if not NewJoineProfile.objects.filter(user=obj.applicant.user).exists():
                NewJoineProfile.objects.create(
                    user=obj.applicant.user,
                    FullName=obj.applicant.FullName,
                    Resume=obj.applicant.Resume,
                    AdharCard=obj.applicant.AdharCard,
                    technology=obj.applicant.technology,
                    Experience=obj.applicant.Experience,
                )

    # -------------------------------
    # PERMISSIONS (same as yours)
    # -------------------------------
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_hr or request.user.is_manager or request.user.is_superuser:
            return qs
        return qs.none()

    def has_change_permission(self, request, obj=None):
        return request.user.is_hr or request.user.is_manager or request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_hr or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_hr or request.user.is_superuser


admin.site.register(HRRequest, HRRequestAdmin)



