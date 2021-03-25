from django.shortcuts import render
from .models import Course,Student
# Create your views here.

def get_students(request):
  return Student.objects.all().order_by('name')

def get_courses(request):
  return Course.objects.all().order_by('crs_id')
  
