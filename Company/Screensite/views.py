
# Screensite/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from Profile.models import NewJoineProfile
from Requests.models import HRRequest

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if user already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'Screensite/signup.html', {'error': 'Email already exists'})

        # Create user
        user = User.objects.create_user(email=email, password=password)
        user.role = 'NJ'
        user.is_NewJoine = True
        user.is_active = True  # make sure the user is active
        user.save()

        # Authenticate and log in the user
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('Screensite:apply')  # Redirect to application form
        else:
            return render(request, 'Screensite/signup.html', {'error': 'Unable to login after signup'})

    return render(request, 'Screensite/signup.html')




def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('Screensite:apply')
        else:
            return render(request, 'Screensite/login.html', {'error': 'Invalid credentials'})
    return render(request, 'Screensite/login.html')




from django.contrib.auth.decorators import login_required

@login_required(login_url='/Screensite/login/')
def newjoinee_apply(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        resume = request.FILES['resume']
        adhar = request.FILES['adhar']
        technology = request.POST['technology']
        experience = request.POST['experience']
        assigner_role = request.POST.get('assigner', 'HR')

        profile = NewJoineProfile.objects.create(
            user=request.user,
            FullName=fullname,
            Resume=resume,
            AdharCard=adhar,
            technology=technology,
            Experience=experience
        )

        # assign HR user
        hr_user = User.objects.filter(role=assigner_role).first()
        HRRequest.objects.create(applicant=profile, hr_user=hr_user)

        return redirect('Screensite:confirmation')

    return render(request, 'Screensite/newjoine_Profile.html')



def confirmation(request):
    return render(request, 'Screensite/confirmation.html')


