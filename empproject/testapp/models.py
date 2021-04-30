from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=30)
    objects=CustomManager()
    
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')
