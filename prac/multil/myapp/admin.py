from django.contrib import admin
from .models import Emp,Coust,Std
# Admin model

class AdminEmp(admin.ModelAdmin):
    list_display=['name','loc']
class AdminCoust(admin.ModelAdmin):
    list_display=['email','address']
class AdminStd(admin.ModelAdmin):
    list_display=['fees']    

# Register your models here.

admin.site.register(Emp,AdminEmp)
admin.site.register(Coust,AdminCoust)
admin.site.register(Std,AdminStd)