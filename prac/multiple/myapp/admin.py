from django.contrib import admin
from .models import Emp,Cst,Std
# Model Admin
class AdminEmp(admin.ModelAdmin):
    list_display=['eid','name','loc']
class AdminCst(admin.ModelAdmin):
    list_display=['cid','email','address']
class AdminStd(admin.ModelAdmin):
    list_display=['fee']    

# Register your models here.

admin.site.register(Emp,AdminEmp)
admin.site.register(Cst,AdminCst)
admin.site.register(Std,AdminStd)