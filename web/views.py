from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from employee.models import Employee
from project_manager.models import ProjectManager
from django.contrib.auth.models import User


def index(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if Employee.objects.filter(user=user).exists():
                role = 'employee'
                login(request, user)
                return redirect('employee/dashboard')
            elif ProjectManager.objects.filter(user=user).exists():
                role = 'project_manager'
                login(request, user)
                return redirect('project-manager/dashboard')
            elif User.objects.filter(username=username).exists():
                role = 'admin'
                login(request, user)
                return redirect('/admin/')
            else:
                message = 'user role not exist'
        else:
            message = 'user role not exist'
    context={
        'message' : message,
    }
    return render(request,'login.html',context)

def logout_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        message = f'Successfully logged out {username}.'
    else:
        message = 'No user was logged in.'
    return redirect('/')
