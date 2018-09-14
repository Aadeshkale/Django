from django.contrib import admin
from .models import Student,Course

# admin model to whole tabel content

class adminStudent(admin.ModelAdmin):
    list_display=['id','name','gender','address']
class adminCourse(admin.ModelAdmin):
    list_display=['id','cname','cfee','student']

# Register your models here.
admin.site.register(Student,adminStudent)
admin.site.register(Course,adminCourse)