from django.urls import path
from . import views

urlpatterns = [
    path('',views.students_list,name='student_list')
]