# Generated by Django 5.0.3 on 2024-03-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0013_alter_project_priority_alter_project_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(blank=True, choices=[('urgent', 'Urgent'), ('normal', 'Normal'), ('high', 'High'), ('low', 'Low')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('on_progress', 'On progress'), ('completed', 'Completed'), ('paused', 'Paused'), ('to_do', 'To do')], max_length=50, null=True),
        ),
    ]