from django.shortcuts import render,redirect
from .models import Student
from .form import StudentForm
# Create your views here.
def students_list(request):
    students = Student.objects.all()
    return render(request,'students/student_list.html',{'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')    
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})