from rest_framework import serializers
from .models import Tasks, OverdueTasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

class OverdueTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverdueTasks
        fields = '__all__'
