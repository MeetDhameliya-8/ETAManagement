
#requests/views.py

from django.shortcuts import render
from .models import HRRequest
from django.contrib.auth.decorators import login_required

@login_required
def hr_request_list(request):
    user = request.user
    if user.is_hr or user.is_manager or user.is_superuser:
        requests = HRRequest.objects.all()
    else:
        requests = HRRequest.objects.none()  # Employees see nothing
    return render(request, 'requests/list.html', {'requests': requests})





