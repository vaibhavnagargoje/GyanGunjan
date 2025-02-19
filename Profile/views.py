from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the frontend
        else:
            return render(request, 'profile/login.html', {'error': 'Invalid credentials'})
    return render(request, 'profile/login.html')

def logout_view(request):
    logout(request)
    return redirect('/profile/login/')

@login_required
def home_view(request):
    return render(request, 'profile/home.html')  # A sample page for testing





from django.http import HttpResponse

def check_auth(request):
    if request.user.is_authenticated:
        return HttpResponse(status=200)
    return HttpResponse(status=403)
