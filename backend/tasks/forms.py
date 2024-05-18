from django import forms
from .models import Tasks

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['start_date', 'overdue', 'title', 'content', 'email']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'overdue': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'content': forms.Textarea(attrs={'maxlength': 500}),
        }
