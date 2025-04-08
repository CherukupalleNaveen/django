from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('attendance/', views.attendance_list, name='attendance_list'),
]
