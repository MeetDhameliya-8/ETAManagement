
# Screensite/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from Profile.models import NewJoineProfile
from Requests.models import HRRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required


User = get_user_model()

'''def signup_view(request):
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
'''




def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if user already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'Screensite/signup.html', {'error': 'Email already exists'})

        # Create user
        user = User.objects.create_user(email=email, password=password)
        user.role = 'NJ'   # mark as new joinee
        user.is_NewJoine = True
        user.is_active = True
        user.save()

        # Authenticate and log in
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




'''@login_required(login_url='/Screensite/login/')
def newjoinee_apply(request):
    if request.method == 'POST':
        # Get form data
        FullName = request.POST.get('FullName')
        Resume = request.FILES.get('Resume')
        AdharCard = request.FILES.get('AdharCard')
        technology = request.POST.get('technology')
        Experience = request.POST.get('Experience')
        assigner_role = request.POST.get('assigner', 'HR')  # default role

        # Create the NewJoineProfile record
        profile = NewJoineProfile.objects.create(
            user=request.user,
            FullName=FullName,
            Resume=Resume,
            AdharCard=AdharCard,
            technology=technology,
            Experience=Experience
        )

        # Try to assign HR user, but do NOT block application if none exists
        hr_user = User.objects.filter(role=assigner_role).first()
        if hr_user:
            HRRequest.objects.create(applicant=profile, hr_user=hr_user)
        else:
            # Optionally, you can log this or notify admin later
            messages.info(request, "Your application is submitted. HR will be assigned soon.")

        # Redirect to confirmation page
        return redirect('Screensite:confirmation')

    return render(request, 'Screensite/newjoine_Profile.html')'''


'''@login_required(login_url='/Screensite/login/')
def newjoinee_apply(request):
    if request.method == 'POST':
        # --- 1️⃣ Collect form data safely ---
        FullName = request.POST.get('FullName')
        Resume = request.FILES.get('Resume')
        AdharCard = request.FILES.get('AdharCard')
        technology = request.POST.get('technology')
        Experience = request.POST.get('Experience')
        assigner_role = request.POST.get('assigner', 'HR')  # default HR role

        # --- 2️⃣ Create or update NewJoineProfile linked to the logged-in user ---
        profile, created = NewJoineProfile.objects.get_or_create(
            user=request.user,
            defaults={
                'FullName': FullName,
                'Resume': Resume,
                'AdharCard': AdharCard,
                'technology': technology,
                'Experience': Experience
            }
        )

        if not created:
            # If profile already exists, update its fields
            profile.FullName = FullName
            profile.Resume = Resume
            profile.AdharCard = AdharCard
            profile.technology = technology
            profile.Experience = Experience
            profile.save()

        # --- 3️⃣ Assign HR user if exists ---
        hr_user = User.objects.filter(role='HR').first()

        # Create HRRequest safely
        if hr_user:
            HRRequest.objects.create(
                applicant=profile,
                hr_user=hr_user
            )
            messages.success(request, "Your application has been submitted to HR.")
        else:
            HRRequest.objects.create(
                applicant=profile   # hr_user left NULL
            )
            messages.info(request, "Your application is submitted. HR will be assigned soon.")

        # --- Redirect ---
        return redirect('Screensite:confirmation')
'''
@login_required(login_url='/Screensite/login/')
def newjoinee_apply(request):
    if request.method == 'POST':
        # --- 1️⃣ Collect form data safely ---
        FullName = request.POST.get('FullName')
        Resume = request.FILES.get('Resume')
        AdharCard = request.FILES.get('AdharCard')
        technology = request.POST.get('technology')
        Experience = request.POST.get('Experience')

        # --- 2️⃣ Create or update NewJoineProfile ---
        profile, created = NewJoineProfile.objects.get_or_create(
            user=request.user,
            defaults={
                'FullName': FullName,
                'Resume': Resume,
                'AdharCard': AdharCard,
                'technology': technology,
                'Experience': Experience
            }
        )

        if not created:
            profile.FullName = FullName
            profile.Resume = Resume
            profile.AdharCard = AdharCard
            profile.technology = technology
            profile.Experience = Experience
            profile.save()

        # --- 3️⃣ Assign HR user ---
        hr_user = User.objects.filter(role='HR').first()

        # Create HRRequest
        if hr_user:
            HRRequest.objects.create(
                applicant=profile,
                hr_user=hr_user
            )
            messages.success(request, "Your application has been submitted to HR.")
        else:
            HRRequest.objects.create(
                applicant=profile   # hr_user = NULL
            )
            messages.info(request, "Your application is submitted. HR will be assigned soon.")

        return redirect('Screensite:confirmation')

    # --- GET request ---
    return render(request, 'Screensite/newjoine_Profile.html')


def confirmation(request):
    return render(request, 'Screensite/confirmation.html')


'''
hr_user = User.objects.filter(role=assigner_role).first() 
 if hr_user: # Create HRRequest linking applicant to HR 
  HRRequest.objects.create(applicant=profile, hr_user=hr_user) 
  messages.success(request, "Your application has been submitted to HR.")
 else: 
messages.info(request, "Your application is submitted. HR will be assigned soon.") # --- 4️⃣ Redirect to confirmation page ---
 return redirect('Screensite:confirmation')
'''