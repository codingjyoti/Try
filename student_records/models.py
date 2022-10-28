
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 50)
    rollno= models.IntegerField()
    subject= models.CharField(max_length = 50)

    def __str__(self):
        return self.name
