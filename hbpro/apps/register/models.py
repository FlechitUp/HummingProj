from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    github = models.CharField(max_length=50)
    is_working = models.BooleanField()
    #subject_student = models.ManyToManyField(Subject)

    def __str__(self):
        return (self.name)
