from django.urls import path

from . import views
from . import views_base

urlpatterns = [
    path('', views.StudentsListView.as_view(), name='students'),
    path('json/', views_base.StudentsListView.as_view(), name='students_list'),
]
