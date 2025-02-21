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
            next_url = request.POST.get('next')
            if not next_url:
                next_url = 'http://localhost:3000'  # Default URL after login
            return redirect(next_url)  # Redirect to frontend after login
        else:
            return render(request, 'profile/login.html', {'error': 'Invalid credentials'})

    next_url = request.GET.get('next', 'http://localhost:3000')  # Capture next from GET params
    return render(request, 'profile/login.html', {'next': next_url})


def custom_logout(request):
    logout(request)
    return redirect('http://localhost:8000/profile/login/?next=http://localhost:3000')



@require_GET
def check_auth(request):
    return JsonResponse({
        'authenticated': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else ''
    })