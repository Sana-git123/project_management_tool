from django.contrib import admin
from employee.models import EmployeeProject,Employee

# Register your models here.
@admin.register(EmployeeProject)
class EmployeeProjectAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project','date_added','updated_by','updated_on', 'assign_date', 'due_date', 'priority', 'project_status')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'mobile_no')  
