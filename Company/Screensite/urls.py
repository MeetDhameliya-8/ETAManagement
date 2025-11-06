# Screensite/urls.py
from django.urls import path
from . import views

app_name = "Screensite"

urlpatterns = [
    path('', views.login_view, name='login'),  # root URL
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('apply/', views.newjoinee_apply, name='apply'),
    path('confirmation/', views.confirmation, name='confirmation'),
]

