
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs = {"type":"date"}))
    class Meta:
        model = Student
        # fields = ["name", "age" , "email"]
        fields = "__all__"

    

