

# Create your views here.
# Create your views here.
from django.shortcuts import redirect, render,get_object_or_404, HttpResponse
from .models import Project, Task
from .decorators import manager_required
from django.contrib.auth.decorators import login_required
from Profile.models import EmployeeProfile, User
from functools import wraps
from .models import Project,EmployeeUpdate,InternUpdate,HrUpdate,NewjoineUpdate
from .forms import EmployeeUpdateForm, InternUpdateForm, NewjoineUpdateForm, HrUpdateForm
from Interactions.forms import CommunicationForm

# below 4 functions are for forms 






def employee_update_view(request):
    updates = EmployeeUpdate.objects.all().order_by("-created_at")

    if request.method == "POST":
        form = EmployeeUpdateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            return redirect("employee_update")
    else:
        form = EmployeeUpdateForm()

    return render(
        request,
        "Projects/employee_u.html",
        {
            "form": form,
            "updates": updates,
            "communication_form": CommunicationForm(),  # 🔑
        }
    )





def intern_update_view(request):
    updates = InternUpdate.objects.all().order_by("-created_at")

    if request.method == "POST":
        form = InternUpdateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            return redirect("intern_update")
    else:
        form = InternUpdateForm()

    return render(
        request,
        "Projects/intern_u.html",
        {
            "form": form,
            "updates": updates,
        }
    )




def newjoinee_update_view(request):
    updates = NewjoineUpdate.objects.all().order_by("-created_at")

    if request.method == "POST":
        form = NewjoineUpdateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            return redirect("newjoinee_update")
    else:
        form = NewjoineUpdateForm()

    return render(
        request,
        "Projects/newjoinee_u.html",
        {
            "form": form,
            "updates": updates,
        }
    )





def hr_update_view(request):
    updates = HrUpdate.objects.all().order_by("-created_at")

    if request.method == "POST":
        form = HrUpdateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            return redirect("hr_update")
    else:
        form = HrUpdateForm()

    return render(
        request,
        "Projects/hr_u.html",
        {
            "form": form,
            "updates": updates,
        }
    )










def manager_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/Screensite/login/')
        
        # Your role check
        if getattr(request.user, "role", None) != "MG":
            return HttpResponse("Unauthorized: Only managers can perform this action.", status=403)

        return view_func(request, *args, **kwargs)

    return _wrapped_view






# if you save decorator there
@login_required(login_url='/Screensite/login/')
@manager_required
def create_project(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")

        project = Project.objects.create(
            title=title,
            description=description,
            deadline=deadline,
            manager=request.user
        )

        return redirect("project:assign_members", project_id=project.id)

    return render(request, "project/create_project.html")







@manager_required
def manager_dashboard(request):
    projects = Project.objects.filter(manager=request.user)
    return render(request, "Projects/manager_dashboard.html", {"projects": projects})



def projects_dashboard(request):
    return render(request, "Projects/pjdash.html")




# Projects/views.py


@login_required(login_url='Screensite:login')
def my_projects(request):
    # show projects where the current user is manager OR part of team — adjust as needed
    projects = Project.objects.filter(manager=request.user).prefetch_related('team_members')
    return render(request, "Projects/my_projects.html", {"projects": projects})







@manager_required
def assign_members(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Fetch only employees (not managers, not interns)
    employees = User.objects.filter(role="Emp")

    if request.method == "POST":
        selected_members = request.POST.getlist("members")

        project.team_members.set(selected_members)
        project.save()

        return redirect("manager_dashboard")

    return render(request, "Projects/assign_members.html", {
        "project": project,
        "employees": employees,
    })





@manager_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)

    return render(request, "projects/project_detail.html", {
        "project": project,
        "tasks": tasks,
    })





@manager_required
def add_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Optional: prevent managers from editing others’ projects
    if project.manager != request.user:
        return HttpResponse("Unauthorized: You cannot add tasks to a project you don't manage.", status=403)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")

        Task.objects.create(
            project=project,
            title=title,
            description=description,
            status=status
        )

        return redirect("project:project_detail", project_id=project.id)

    return render(request, "projects/add_task.html", {"project": project})

























