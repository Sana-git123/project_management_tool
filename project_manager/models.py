from django.db import models
from django.utils.translation import gettext_lazy as _
from employee.models import Employee,EmployeeProject
from django.contrib.auth.models import User

PROJECT_PRIORITY_CHOICES = {
        ('urgent', 'Urgent'),
        ('high', 'High'),
        ('normal', 'Normal'),
        ('low', 'Low'),
    }
PROJECT_STATUS_CHOICES = {
        ('on_progress', 'On progress'),
        ('completed', 'Completed'),
        ('to_do', 'To do'),
        ('paused', 'Paused'),
        ('over_due', 'Overdue'),
    }

class Project(models.Model):
    name = models.CharField(max_length=256)
    start_date = models.DateTimeField(null=True,blank=True)
    submission_date = models.DateTimeField(null=True,blank=True)
    description = models.TextField()    
    priority = models.CharField(choices=PROJECT_PRIORITY_CHOICES,null=True,blank=True)    
    project_status = models.CharField(choices=PROJECT_STATUS_CHOICES,null=True,blank=True)
    team_lead = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)
    client_name = models.CharField(max_length=256,null=True,blank=True)
    client_email = models.CharField(max_length=256,null=True,blank=True)
    client_contact_number = models.CharField(max_length=20,null=True,blank=True)
    project_manager = models.ForeignKey('project_manager.ProjectManager',on_delete=models.CASCADE,null=True)


    class Meta:
        db_table = 'project_manager_project'
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ('submission_date',)

    def __str__(self):
        return self.name

    
class ProjectManager(models.Model):
    name = models.CharField(max_length=156)
    userid = models.CharField(max_length=156)
    password = models.CharField(max_length=156)
    mobile_number = models.CharField(max_length=156)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    project_manager_project = models.ManyToManyField(Project,null=True,blank=True)
    profile_image=models.ImageField(upload_to='profile_images/',null=True,blank=True)

    class Meta:
        db_table = 'project_manager_project_manger'
        verbose_name = _('project manager')
        verbose_name_plural = _('project managers')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    employee = models.ForeignKey('employee.employee',on_delete=models.CASCADE,null=True,blank=True,related_name='profile_meetings')
    meet_date = models.DateTimeField(null=True,blank=True)
    link = models.CharField(max_length=700,null=True,blank=True)
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('project_manager.projectmanager',on_delete=models.CASCADE,null=True,blank=True,related_name='created_meetings')

    class Meta:
        db_table = 'project_manager_meeting'
        verbose_name = _('Meeting')
        verbose_name_plural = _('Meetings')
        ordering = ('-meet_date',)

    def __str__(self):
        return str(self.employee)
    
    