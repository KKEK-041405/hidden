from django import forms
from .models import StudentInfo
class StudentDetaislForm(forms.ModelForm):

    class Meta:
        model = StudentInfo
        fields = "__all__"
        
    """StudentDetaislForm definition."""

