from django.contrib import admin
from myapp.models import *
# Register your models here.

class  AdminStudent(admin.ModelAdmin):
    list_display=['id','name','age']

class AdminSubject(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Student,AdminStudent)
admin.site.register(Subject,AdminSubject)