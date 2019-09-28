from django.contrib import admin

from django.urls import path

from application.views import home

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home, name='home')
]
