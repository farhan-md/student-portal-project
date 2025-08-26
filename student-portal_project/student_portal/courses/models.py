from django.db import models

# Create your models here.
class course(models.Model):
    name = models.CharField(max_length=100)
    credit = models.IntegerField()


    def __str__(self):
        return self.name