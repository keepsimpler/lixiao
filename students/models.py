from django.db import models


# 学生所在院系的信息
class School(models.Model):
    code = models.CharField('院系编码', max_length=20)  # 院系编码
    name = models.CharField('院系全称', max_length=100)  # 院系全称
    jc = models.CharField('院系简称', max_length=50)  # 院系简称

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '院系'


# 学生所属专业信息
class Department(models.Model):
    code = models.CharField('专业编码', max_length=20)  # 专业编码
    name = models.CharField('专业全称', max_length=100)  # 专业全称
    jc = models.CharField('专业简称', max_length=50)  # 专业简称

    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='所属院系')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '专业'


# 学生所在年级信息
class Grade(models.Model):
    code = models.CharField('年级编码', max_length=20)  # 年级编码
    name = models.CharField('年级全称', max_length=100)  # 年级全称
    jc = models.CharField('年级简称', max_length=50)  # 年级简称

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '年级'


# 学生所属班级信息
class Team(models.Model):
    code = models.CharField('班级编码', max_length=20)  # 班级编码
    name = models.CharField('班级全称', max_length=100)  # 班级全称
    jc = models.CharField('班级简称', max_length=50)  # 班级简称

    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='所属专业')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='所在年级')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '班级'


# 学生信息
class Student(models.Model):
    name = models.CharField('姓名', max_length=200)  # 学生姓名
    code = models.CharField('学号', max_length=50)  # 学号（或一卡通号）
    # enter_year = models.IntegerField('入学年度')  # 入学年度
    # graduate_year = models.IntegerField('毕业年度')  # 毕业年度

    # school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='所属院系')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='所属班级')

    tushu_flag = models.BooleanField('是否正常还书')  #
    caiwu_flag = models.BooleanField('是否缴费')
    sushe_flag = models.BooleanField('是否退宿')
    grad_flag = models.BooleanField('是否已发放毕业证')

    class Meta:
        verbose_name_plural = '毕业生信息'

    def __str__(self):
        return self.name


