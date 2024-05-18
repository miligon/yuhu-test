from django.contrib import admin
from .models import Tasks, OverdueTasks

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'created_at', 'overdue')
    search_fields = ('title', 'email')
    list_filter = ('created_at', 'overdue')
    ordering = ('-created_at',)

@admin.register(OverdueTasks)
class OverdueTasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'created_at', 'overdue')
    search_fields = ('title', 'email')
    list_filter = ('created_at', 'overdue')
    ordering = ('-created_at',)
