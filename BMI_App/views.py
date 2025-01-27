from django.shortcuts import render, redirect
from django.http import HttpResponse
#from BMI_App.utils import detectUser
from .forms import UserForm
from .models import User, UserProfile
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .utils import detectUser  # Import the function


# Create your views here

def home(request):
    # Render the index.html template
    return render(request, 'home.html')

def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('calculator')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
        else:
            print(form.errors)

    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'BMI_App/registerUser.html', context)






def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(f"Attempting login for email: {email}, password: {password}")  # Debug

        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        
        if user:
            print(f"Authenticated user: {user.email}")
        else:
            print("Authentication failed.")
        
        if user is not None:
            auth_login(request, user)
            
            # Check if the user is authenticated (debugging)
            if user.is_authenticated:
                print(f'User {user.email} successfully logged in.')
                

            # Redirect based on user role
            if user.is_superuser:  # Redirect superusers to the admin panel
                print(f"Superuser {user.email} redirected to /admin")
                return redirect('/admin')
            else:
                print(f"User {user.email} redirected to calculator")
                messages.success(request, 'You are now logged in!')
                return redirect('calculator')
                
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')

    return render(request, 'BMI_App/login.html')


def calculator(request):
    # Render the calculate.html template
  
    return render(request, 'BMI_App/calculator.html')

def result(request):
    # Retrieve query parameters
    age = request.GET.get('age')
    bmi = request.GET.get('bmi')
    status = request.GET.get('status')
    comments = request.GET.get('comments', '')

    # Validate parameters
    if not age or not bmi or not status:
        return render(request, 'BMI_App/result.html', {'error': 'Missing required fields.'})

    # Pass data to the result template
    context = {
        'age': age,
        'bmi': bmi,
        'status': status,
        'comments': comments,
    }
    return render(request, 'BMI_App/result.html', context)


# For logout

def logout(request):
    auth.logout(request)
    messages.info(request, 'logged out!')
    return redirect('login')



# My Account

@login_required(login_url='login')
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)


# For dashboard
@login_required(login_url='login')
def dashboard(request):
     return render(request, 'BMI_App/dashboard.html')
 
 
 





