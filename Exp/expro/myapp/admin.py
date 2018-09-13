from django.contrib import admin
from .models import Student


class AdminStudent(admin.ModelAdmin):
    list_display=['id','name','age','email','address']


# Register your models here.
admin.site.register(Student,AdminStudent)