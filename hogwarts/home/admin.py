from django.contrib import admin
from home.models import Faculty
from home.models import Student
from home.models import Subject, Result

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Result)