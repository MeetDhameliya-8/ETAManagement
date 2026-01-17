
from django.db import models
from django.conf import settings
from Profile.models import NewJoineProfile




'''class HRRequest(models.Model):

    hr_user = models.ForeignKey(

    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,          # <— important
    blank=True,         # <— for admin forms
    related_name='Requests'

    )
 
    applicant = models.ForeignKey(
        NewJoineProfile,
        on_delete=models.CASCADE,
        related_name='Requests'
    )

    STATUS = [

        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),

    ]

    status = models.CharField(max_length=10, choices=STATUS, default='PENDING')

    remarks = models.TextField(blank=True)
    
    reviewed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.applicant.FullName} - {self.status}"
'''


class HRRequest(models.Model):

    hr_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='Requests'
    )

    applicant = models.ForeignKey(
        NewJoineProfile,
        on_delete=models.CASCADE,
        related_name='Requests'
    )

    STATUS = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    status = models.CharField(max_length=10, choices=STATUS, default='PENDING')

    remarks = models.TextField(blank=True)

    reviewed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.applicant.FullName} - {self.status}"



