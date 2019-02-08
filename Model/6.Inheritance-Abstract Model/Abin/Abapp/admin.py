from django.contrib import admin
from .models import Student,Employee,Coustmer

# creating admin model for to see hole table

class AdminStudent(admin.ModelAdmin):
    list_display=['name','loc','fee']
class AdminCourse(admin.ModelAdmin):
    list_display=['name','loc','sales']
class AdminEmployee(admin.ModelAdmin):
    list_display=['name','loc','salary']
    
# Register your models here.

admin.site.register(Student)
admin.site.register(Coustmer)
admin.site.register(Employee)