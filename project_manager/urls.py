from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('projects',views.project,name='project'),
    path('main-projects/',views.main_project,name='main_project'),
    path('meetings/',views.meetings,name='meetings'),
    path('create-meeting/',views.create_meeting,name='create_meeting'),
    path('projects/info/<int:employee_project_id>',views.employee_project_info,name='project_single_info'),
    path('projects/<int:project_id>' ,views.single,name='single'),
    path('empty-project',views.empty,name='empty'),
    path('projects/edit/<int:id>',views.edit,name='edit'),  
    path('projects/create',views.create,name='create'),
    path('projects/task',views.task,name='task'),
    path('projects/cancel-url',views.cancelCreate,name='cancel_url'),
    # path('projects/cancel-task',views.cancelTask,name='cancel_task_url'),
]