from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classes/<int:class_id>/', views.class_detail, name='class_detail'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
]
