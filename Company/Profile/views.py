# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # create user with role='NewJoinee'
        user = User.objects.create_user(email=email, password=password)
        user.role = 'NewJoinee'
        user.is_NewJoine = True
        user.save()
        return redirect('apply')  # redirect to application form
    return render(request, 'registration/signup.html')