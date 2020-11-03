from django.db import models

# Create your models here.
class student(models.Model):
    student_sno = models.IntegerField();
    student_name = models.CharField(max_length=256);
    student_father_name= models.CharField(max_length=256);

class student_class(models.Model):
    student = models.ForeignKey(student,on_delete=models.CASCADE) 




