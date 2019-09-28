from django.db import models

# Create your models here

class Employees(models.Model):
    name = models.CharField(max_length=128)
    
    email = models.EmailField(max_length=256)
    
    department = models.CharField(max_length=128)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Employees"