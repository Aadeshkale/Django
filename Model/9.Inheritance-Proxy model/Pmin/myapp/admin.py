from django.contrib import admin
from .models import Sproxy,Student

# admin model for Student , Sproxy

class AdminStudent(admin.ModelAdmin):
    list_display=['sid','name','email','address'] 


class AdminSproxy(admin.ModelAdmin):
    list_display=['sid','name','email','address'] 


# Register your models here.

admin.site.register(Student,AdminStudent)
admin.site.register(Sproxy,AdminSproxy)