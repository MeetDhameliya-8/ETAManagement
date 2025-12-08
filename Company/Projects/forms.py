# Projects/forms.py
from django import forms
from .models import EmployeeUpdate, InternUpdate, NewjoineUpdate, HrUpdate


class EmployeeUpdateForm(forms.ModelForm):
    Deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            "type": "datetime-local",
            "class": "form-control",
        }),
        input_formats=["%Y-%m-%dT%H:%M"]
    )

    class Meta:
        model = EmployeeUpdate
        fields = ["Project", "task", "description", "Things_To_Notice", "Deadline"]
        widgets = {
            "Project": forms.TextInput(attrs={"class": "form-control"}),
            "task": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "Things_To_Notice": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class InternUpdateForm(forms.ModelForm):
    class Meta:
        model = InternUpdate
        fields = ["Project", "LearnToday", "Source", "WorkWith"]
        widgets = {
            "Project": forms.TextInput(attrs={"class": "form-control"}),
            "LearnToday": forms.TextInput(attrs={"class": "form-control"}),
            "Source": forms.TextInput(attrs={"class": "form-control"}),
            "WorkWith": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class NewjoineUpdateForm(forms.ModelForm):
    class Meta:
        model = NewjoineUpdate
        fields = ["Announcement", "FieldToDecide", "BePreparedFor"]
        widgets = {
            "Announcement": forms.TextInput(attrs={"class": "form-control"}),
            "FieldToDecide": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "BePreparedFor": forms.TextInput(attrs={"class": "form-control"}),
        }


class HrUpdateForm(forms.ModelForm):
    class Meta:
        model = HrUpdate
        fields = ["taskUpdate", "NewRule", "Notice", "Celebration", "Preparation"]
        widgets = {
            "taskUpdate": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "NewRule": forms.TextInput(attrs={"class": "form-control"}),
            "Notice": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "Celebration": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "Preparation": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

