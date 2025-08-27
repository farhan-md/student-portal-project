from django.shortcuts import render
from .models import Student
# Create your views here.
def students_list(request):
    students = Student.objects.all()
    return render(request,'students/student_list.html',{'students': students})