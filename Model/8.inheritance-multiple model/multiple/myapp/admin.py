from django.contrib import admin
from .models import Student,Coustmer,Employee

# admin model
class AdminStudent(admin.ModelAdmin):
    list_display=['name','loc','fee']


# Register your models here.

admin.site.register(Coustmer)
admin.site.register(Employee)
admin.site.register(Student,AdminStudent)