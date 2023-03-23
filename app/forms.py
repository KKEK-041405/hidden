from django import forms
from .models import StudentInfo,AdditionalDetails

class StudentDetaislForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = "__all__"
        
class GetStudentDetails(forms.Form):
    csvfile = forms.FileField()

class UpdateStdDetails(forms.ModelForm):
    class Meta:
        model = AdditionalDetails
        fields = "__all__"
    

    """StudentDetaislForm definition."""

