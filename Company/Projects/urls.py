from django.urls import path, include
from . import views

app_name = "Projects"

urlpatterns = [

    path('dashboard/', views.manager_dashboard, name='manager_dashboard'),   
    path('projects/', views.my_projects, name='my_projects'), 
    path('project/create/', views.create_project, name='create_project'),
    path('project/<int:project_id>/assign/', views.assign_members, name='assign_members'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'), 
    path('project/<int:project_id>/task/add/', views.add_task, name='add_task'),


    #forms

    path("employee/update/",views.employee_update_view, name="employee_update"),
    path("intern/update/", views.intern_update_view, name="intern_update"),
    path("newjoinee/update/",views.newjoinee_update_view, name="newjoinee_update"),
    path("hr/update/", views.hr_update_view, name="hr_update"),  

]




