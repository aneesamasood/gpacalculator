# gpaapp/urls.py
from django.urls import path
from . import views

app_name = 'gpaapp'

urlpatterns = [
    path('', views.calculate_gpa, name='calculate_gpa'),
    # You can add more parameters to the path if needed, for example:
    # path('calculate_gpa/<int:student_id>/', views.calculate_gpa, name='calculate_gpa'),
]

