from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','course']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("email should ends with (@gmail.com)")
        return email