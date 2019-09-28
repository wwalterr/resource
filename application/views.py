from django.shortcuts import render, redirect

from rest_framework import viewsets, permissions

# Create your views here

def home(request):
    return redirect('/admin')

# View sets define the view behavior

class EmployeesViewSet(viewsets.ModelViewSet):
    from .serializers import EmployeesSerialize
    
    from .models import Employees
    
    queryset = Employees.objects.all()
    
    serializer_class = EmployeesSerialize
    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)