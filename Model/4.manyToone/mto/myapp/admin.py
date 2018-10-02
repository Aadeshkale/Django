from django.contrib import admin
from .models import Student,Course

# Creating Admin Modals for Student , Course Tables
# To See All Tabel content

class AdminStudent(admin.ModelAdmin):
    list_display=['sid','name','location']

class AdminCourse(admin.ModelAdmin):
    list_display=['cname','student']

# Register your models here.

admin.site.register(Student,AdminStudent)
admin.site.register(Course,AdminCourse)