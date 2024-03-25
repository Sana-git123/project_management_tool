# Generated by Django 5.0.3 on 2024-03-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0024_alter_employee_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, choices=[('devops_engineer', 'Devops Engineer'), ('ui_ux_designing', 'UX / UI Designing'), ('web_development', 'Web Development'), ('mobile_app_development', 'Mobile App Development')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('low', 'Low'), ('urgent', 'Urgent'), ('high', 'High'), ('normal', 'Normal')], null=True),
        ),
        migrations.AlterField(
            model_name='employeeproject',
            name='project_status',
            field=models.CharField(blank=True, choices=[('completed', 'Completed'), ('to_do', 'To do'), ('paused', 'Paused'), ('on_progress', 'On progress')], null=True),
        ),
    ]