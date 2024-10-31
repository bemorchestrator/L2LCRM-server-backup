from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            return HttpResponse("Invalid login credentials", status=401)
    return render(request, 'IAM/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'IAM/dashboard.html')