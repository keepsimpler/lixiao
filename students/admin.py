from django.contrib import admin

from .models import School, Student, Department, Grade, Team

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Grade)
admin.site.register(Team)
