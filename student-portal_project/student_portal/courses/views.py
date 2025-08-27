from django.shortcuts import render
from .models import course
# Create your views here.
def course_list(request):
    courses = course.objects.all()
    return render(request,'courses/course_list.html',{'courses': courses})
