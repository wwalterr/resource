from django.contrib import admin

from django.urls import path, include

from application.views import home

from application.views import EmployeesViewSet

from rest_framework import routers

# Set the URL configuration to the employees
router = routers.DefaultRouter() 

router.register('employees', EmployeesViewSet)

# Rest framework is required only if the browsable API is
# being used
urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls), name='employees'),
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('rest_framework.urls'))
]
