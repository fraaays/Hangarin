from django import forms
from .models import Task, SubTask, Note, Category, Priority

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"

class PriorityForm(forms.ModelForm):

    class Meta:
        model = Priority
        fields = "__all__"

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.Textarea(attrs={'class': 'form-control'}),
                'deadline': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
                'status': forms.Select(attrs={'class': 'form-select'}),
                'category': forms.Select(attrs={'class': 'form-select'}),
                'priority': forms.Select(attrs={'class': 'form-select'}),
            }

class SubTaskForm(forms.ModelForm):

    class Meta:
        model = SubTask
        fields = "__all__"

        widgets = {
            'parent_task': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = "__all__"

        widgets = {
            'task': forms.Select(attrs={
                'class': 'form-select'
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Write your note here...'
            }),
        }