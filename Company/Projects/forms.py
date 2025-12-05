# forms.py
from django import forms
from .models import EmployeeUpdate, InternUpdate, NewjoineUpdate, HrUpdate

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeeUpdate
        fields = ['Project', 'task', 'description', 'Things_To_Notice', 'Deadline']
        widgets = {
            'Project': forms.TextInput(attrs={'placeholder': 'Project name or code'}),
            'task': forms.TextInput(attrs={'placeholder': 'Task title'}),
            'description': forms.Textarea(attrs={'rows':4}),
            'Things_To_Notice': forms.Textarea(attrs={'rows':3}),
            'Deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        help_texts = {
            'Things_To_Notice': 'Important notes for employees',
        }

class InternUpdateForm(forms.ModelForm):
    class Meta:
        model = InternUpdate
        fields = ['Project', 'LearnToday', 'Source', 'WorkWith']
        widgets = {
            'Project': forms.TextInput(),
            'LearnToday': forms.TextInput(),
            'Source': forms.TextInput(),
            'WorkWith': forms.Textarea(attrs={'rows':3}),
        }

class NewjoineUpdateForm(forms.ModelForm):
    class Meta:
        model = NewjoineUpdate
        fields = ['Announcement', 'FieldToDecide', 'BePreparedFor']
        widgets = {
            'Announcement': forms.TextInput(),
            'FieldToDecide': forms.Textarea(attrs={'rows':3}),
            'BePreparedFor': forms.TextInput(),
        }

class HrUpdateForm(forms.ModelForm):
    class Meta:
        model = HrUpdate
        fields = ['taskUpdate', 'NewRule', 'Notice', 'Celebration', 'Preparation']
        widgets = {
            'taskUpdate': forms.Textarea(attrs={'rows':4}),
            'NewRule': forms.TextInput(),
            'Notice': forms.Textarea(attrs={'rows':3}),
            'Celebration': forms.Textarea(attrs={'rows':2}),
            'Preparation': forms.Textarea(attrs={'rows':2}),
        }
