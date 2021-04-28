from django.db import models
from django.contrib.auth.models import User

class Marker(User):
    account_type = models.CharField(default = 'marker', max_length = 20)
    class Meta:
        verbose_name = 'marker'
        verbose_name_plural = 'markers'

    def __str__(self):
        return self.username

class Student(User):
    account_type = models.CharField(default = 'student', max_length = 20)
    
    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
    
    def __str__(self):
        return self.username


class Task(models.Model):
    title = models.CharField(max_length = 50)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    marker = models.ForeignKey(Marker, on_delete = models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add = True)
    attachment = models.FileField(upload_to = 'attachments', null = True)
    marked = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
