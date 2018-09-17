from django.contrib import admin
from .models import Student,Course

# Admin models for to see whole tabels  

class AdminStudent(admin.ModelAdmin):
   list_display=['name','age','loc'] 

class AdminCourse(admin.ModelAdmin):
    list_display=['cname','cfee']
    
# Register your models here.

admin.site.register(Student)
admin.site.register(Course)

