from django import forms
from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['date', 'status']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}
