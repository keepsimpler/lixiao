from .models import Student, School, Department, Team
from rest_framework import serializers


class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    school_name = serializers.SerializerMethodField(read_only=True)
    department_name = serializers.SerializerMethodField(read_only=True)
    team_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = ('name', 'code', 'school_name', 'department_name', 'team_name',
                  'caiwu_flag', 'tushu_flag', 'sushe_flag', 'grad_flag')

    def get_school_name(self, student):
        return student.team.department.school.name

    def get_department_name(self, student):
        return student.team.department.name

    def get_team_name(self, student):
        return student.team.name