from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

from .models import Student, School, Department, Team
from .serializers import StudentsSerializer


class StudentsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'  # 动态改变每页记录数时，前端传递的参数名称
    page_query_param = 'page'  # 获得当前页码时，前端传递的参数名称
    max_page_size = 100  # 最多能显示多少页


class StudentsListView(generics.ListAPIView):
    queryset = Student.objects.select_related('team__department__school').order_by('id')
    serializer_class = StudentsSerializer
    pagination_class = StudentsPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ('=team__department__school__name',)
