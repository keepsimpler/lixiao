from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("你好！你已经进入了学生应用。")