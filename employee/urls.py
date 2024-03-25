from django.urls import path
from.import views

urlpatterns = [
    
    path('dashboard',views.employeeDashboard,name='employeeDashboard'),
    path('projects',views.employeeProject,name='employeeProject'),
    path('projects/<int:project_id>',views.employeeSingleProject,name='updateProject'),
    path('projects/update/<int:id>', views.updateProject, name='update'),
]