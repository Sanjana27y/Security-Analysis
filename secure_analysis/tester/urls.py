from django.contrib import admin
from django.urls import path, include
from tester import views
from .views import test_directory_traversal_endpoint, test_directory_traversal, test_xxe, test_security_misconfigurations,test_xss

urlpatterns = [
    path('',views.index, name='home'),
    path('test_directory_traversal_endpoint', views.test_directory_traversal_endpoint, name='test_directory_traversal_endpoint'),
    # path('analyser/', views.analyser, name='analyser'),
  ]
