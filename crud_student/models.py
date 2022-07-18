from django.db import models

# Create your models here.
class student(models.Model):
    Name = models.CharField(max_length=100)
    FatherName = models.CharField(max_length=100)
    Roll = models.CharField(max_length=10)
    phn_no = models.CharField(max_length=12)