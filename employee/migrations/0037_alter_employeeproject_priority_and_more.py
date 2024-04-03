# Generated by Django 5.0.3 on 2024-04-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0036_alter_employee_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('normal', 'Normal'), ('urgent', 'Urgent'), ('high', 'High'), ('low', 'Low')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='project_status',
            field=models.CharField(blank=True, choices=[('on_progress', 'On progress'), ('to_do', 'To do'), ('over_due', 'Overdue'), ('completed', 'Completed'), ('paused', 'Paused')], null=True),
        ),
    ]