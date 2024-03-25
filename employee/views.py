from django.shortcuts import render,redirect
from project_manager.models import Project
from employee.models import EmployeeProject
from datetime import date,datetime

def employeeDashboard(request):
    current_user = request.user
    all_projects_count = EmployeeProject.objects.filter(employee__user=current_user).count()
    completed_projects_count = EmployeeProject.objects.filter(employee__user=current_user,project_status="completed").count()
    progress_projects_count = EmployeeProject.objects.filter(employee__user=current_user,project_status="on_progress").count()
    overdue_projects_count = EmployeeProject.objects.filter(employee__user=current_user,project_status="over_due").count()

    today_assigned_projects = EmployeeProject.objects.filter(employee__user=current_user,assign_date__date=datetime.today())

    
    context = {
        'current_user' : current_user,
        'all_projects_count' : all_projects_count,
        'completed_projects_count' : completed_projects_count,
        'progress_projects_count' : progress_projects_count,
        'overdue_projects_count' : overdue_projects_count,
        'today_assigned_projects' : today_assigned_projects,
    }

    return render(request,'employeeDashboard.html',context)


def employeeProject(request):
    current_user = request.user
    project_status = request.GET.get('status')
    all_projects = None

    print(project_status)
    if project_status == 'all':
        all_projects = EmployeeProject.objects.filter(employee__user=current_user)
    elif project_status == 'completed':
        all_projects = EmployeeProject.objects.filter(employee__user=current_user, project_status="completed")
    elif project_status == 'in-progress':
        all_projects = EmployeeProject.objects.filter(employee__user=current_user, project_status="on_progress")
    elif project_status == 'overdue':
        all_projects = EmployeeProject.objects.filter(employee__user=current_user, project_status="over_due")

    context = {
        'current_user' : current_user,
        'all_projects': all_projects,
    }

    return render(request,'employeeProject.html',context)

def employeeSingleProject(request,project_id):
    current_user = request.user
    try:
        singleEmployeeProject = EmployeeProject.objects.get(pk=project_id)
    except:
        return render(request,'emptyProject.html')
    
    context = {
        'current_user' : current_user,
        'singleEmployeeProject' : singleEmployeeProject
    }
    return render(request,'employeeSingleProject.html',context)

def updateProject(request, id):
    current_user = request.user

    redirection_uri = request.GET.get("redirection_uri",f"/employee/projects/{id}")

    description = request.POST.get('description')
    progress = request.POST.get('project_status')
    project = EmployeeProject.objects.get(id=id)
    project.description = description
    project.project_status = progress
    project.save()

    return redirect(to=redirection_uri)

    # try:
    #     singleEmployeeProject = EmployeeProject.objects.get(pk=id)
    # except:
    #     return render(request,'emptyProject.html')
    
    # context = {
    #     'current_user' : current_user,
    #     'singleEmployeeProject' : singleEmployeeProject
    # }

    # return render(request,'employeeSingleProject.html',context)


    
    
