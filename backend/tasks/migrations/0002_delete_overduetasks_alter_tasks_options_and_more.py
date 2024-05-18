# Generated by Django 5.0.3 on 2024-05-18 01:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OverdueTasks',
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AddField(
            model_name='tasks',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='content',
            field=models.TextField(max_length=500, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion:'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='overdue',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de vencimiento'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]
