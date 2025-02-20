from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_GET

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', 'http://localhost:3000')
            return redirect(next_url)
        else:
            return render(request, 'Profile/login.html', {'error': 'Invalid credentials'})
    
    next_url = request.GET.get('next', 'http://localhost:3000')
    return render(request, 'Profile/login.html', {'next': next_url})

def custom_logout(request):
    logout(request)
    return redirect('http://localhost:8000/profile/login/')

@require_GET
def check_auth(request):
    return JsonResponse({
        'authenticated': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else ''
    })