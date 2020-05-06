from django.db import models


# 学生所在院系的信息
class School(models.Model):
    school_text = models.CharField('院系全称', max_length=200)  # 院系全称
    school_jc = models.CharField('院系简称', max_length=100)  # 院系简称

    def __str__(self):
        return self.school_text


# 学生信息
class Student(models.Model):
    student_name = models.CharField('姓名', max_length=200)  # 学生姓名
    student_code = models.CharField('学号', max_length=50)  # 学号（或一卡通号）
    enter_year = models.IntegerField('入学年度')  # 入学年度
    graduate_year = models.IntegerField('毕业年度')  # 毕业年度

    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='所属院系')

    tushu_flag = models.BooleanField('图书是否正常')  #
    caiwu_flag = models.BooleanField('是否缴费')
    sushe_flag = models.BooleanField('是否退宿')

    def __str__(self):
        return self.student_name