from django.contrib import admin
from .models import Coustmer,Employee,Student
# admin models

class AdminCoustmer(admin.ModelAdmin):
    list_display=['cname','csals']

class AdminEmployee(admin.ModelAdmin):
    list_display=['ename','esal']

class AdminStudent(admin.ModelAdmin):
    list_display=['sname','sfee']


# Register your models here.

admin.site.register(Coustmer,AdminCoustmer)
admin.site.register(Employee,AdminEmployee)
admin.site.register(Student,AdminStudent)