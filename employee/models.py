from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

EMPLOYEE_DESIGNATION_CHOICES = {
    ('ui_ux_designing', 'UX / UI Designing'),
    ('mobile_app_development', 'Mobile App Development'),
    ('devops_engineer', 'Devops Engineer'),
    ('web_development', 'Web Development'),
    }
EMPLOYEE_PROJECT_PRIORITY_CHOICES = {
    ('urgent', 'Urgent'),
    ('high', 'High'),
    ('normal', 'Normal'),
    ('low', 'Low'),
}
EMPLOYEE_PROJECT_STATUS_CHOICES = {
    ('on_progress', 'On progress'),
    ('completed', 'Completed'),
    ('to_do', 'To do'),
    ('paused', 'Paused'),
    ('over_due', 'Overdue'),
}


class Employee(models.Model):
    name = models.CharField(max_length=256)
    designation = models.CharField(choices=EMPLOYEE_DESIGNATION_CHOICES,null=True,blank=True)
    mobile_no = models.CharField(max_length=256)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    password = models.CharField(max_length=110)
    profile_image=models.ImageField(upload_to='profile_images/',null=True,blank=True)

    class Meta:
        db_table = 'employee_employee'
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ('name',)

    def __str__(self):
        return self.name
    

class EmployeeProject(models.Model):
    employee = models.ForeignKey('employee.Employee',on_delete=models.CASCADE,null=True,blank=True)
    project = models.ForeignKey('project_manager.Project',on_delete=models.CASCADE,null=True,blank=True)
    date_added = models.DateTimeField(null=True,blank=True)
    assign_date = models.DateTimeField(null=True,blank=True)
    due_date = models.DateTimeField(null=True,blank=True)
    priority = models.CharField(choices=EMPLOYEE_PROJECT_PRIORITY_CHOICES,null=True,blank=True)
    project_status = models.CharField(choices=EMPLOYEE_PROJECT_STATUS_CHOICES,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    updated_on = models.DateField(auto_now=True)
    file_field = models.FileField(upload_to='assets/',null=True,blank=True)
    employee_file = models.FileField(upload_to='completed-work/',null=True,blank=True)

    class Meta:
        db_table = 'employee_employee_project'
        verbose_name = _('Employee Project')
        verbose_name_plural = _('Employee Projects')
        ordering = ('due_date',)

    def __str__(self):
        return str(self.priority)
    
    
