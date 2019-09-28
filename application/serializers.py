from rest_framework import serializers

from .models import Employees

# Serializers define the API representation

class EmployeesSerialize(serializers.ModelSerializer):
    class Meta:
        model = Employees
        
        fields = ['name', 'email', 'department']