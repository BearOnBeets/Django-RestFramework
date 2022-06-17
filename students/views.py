from django.core import serializers
from .models import Student,University
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UniversitySerializer,StudentSerializer
from rest_framework import viewsets

class UniversityViewset(viewsets.ModelViewSet):
    serializer_class=UniversitySerializer
    queryset=University.objects.all() 

class StudentViewset(viewsets.ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all() 
        

