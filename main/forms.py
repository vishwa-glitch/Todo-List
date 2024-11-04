from django import forms
from .models import ToDoList

class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['name', 'description']
        labels = {
            'name': 'Title',
            'description': 'Motto',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'A motto for your motivaton (optional)'}),
        }
