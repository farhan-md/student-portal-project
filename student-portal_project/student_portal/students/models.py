from django.db import models
from courses.models import course
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.ForeignKey(course,on_delete=models.CASCADE)


    def __str__(self):
        return self.name