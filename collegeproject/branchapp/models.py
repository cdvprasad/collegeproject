from django.db import models

# Create your models here.

class StudentInfo(models.Model):

    student = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    phone_no = models.IntegerField(default=0)


class StudentDepartment(models.Model):

    department = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=100)
