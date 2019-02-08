from django.contrib import admin
from .models import Student
# moedel Admin
class AdminStudent(admin.ModelAdmin):
    list_display=['name','address','age']

# Register your models here.
admin.site.register(Student)
