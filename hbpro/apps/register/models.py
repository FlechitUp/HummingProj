from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password_confir = models.CharField(max_length=50)
    age = models.IntegerField()
    e_mail = models.CharField(max_length=50)
    number_phone = models.IntegerField()
    github = models.CharField(max_length=50)
    is_working = models.BooleanField(default=True)
    #subject_student = models.ManyToManyField(Subject)

    def __str__(self):
        return (self.name)
