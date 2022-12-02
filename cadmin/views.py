from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('/admin/dashboard')
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.filter(username=username)
            if not user.exists():
                messages.info(request, 'Account not found')
                return redirect('/')
            user  = authenticate(username=username, password=password)
            if user and user.is_superuser:
                login(request, user)
                return redirect('/admin/dashboard')
            messages.info(request, 'invalid creds')
            return redirect('/')
        return render(request, 'cadmin/index.html')

    except Exception as e:
        print(e)


def dashboard(request):
    return render(request, 'cadmin/dashboard.html')