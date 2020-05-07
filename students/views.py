from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import generics

from .models import Student, School, Department, Team
from .serializers import StudentsSerializer


class StudentsListView(generics.ListAPIView):
    queryset = Student.objects.select_related('team__department__school')
    serializer_class = StudentsSerializer
