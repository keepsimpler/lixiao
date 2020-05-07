import json

from django.http import HttpResponse
from django.views.generic import View
from .models import Student, School, Department, Team


class StudentsListView(View):
    def get(self, request):
        json_list = []
        students = Student.objects.select_related('team__department__school')
        for student in students:
            json_dict = {}
            json_dict['student_name'] = student.name
            json_dict['student_code'] = student.code
            json_dict['school_name'] = student.team.department.school.name
            json_dict['department_name'] = student.team.department.name
            json_dict['team_name'] = student.team.name
            json_dict['caiwu_flag'] = student.caiwu_flag
            json_dict['tushu_flag'] = student.tushu_flag
            json_dict['sushe_flag'] = student.sushe_flag
            json_dict['grad_flag'] = student.grad_flag
            json_list.append(json_dict)

            return  HttpResponse(json.dumps(json_list), content_type='application/json')
