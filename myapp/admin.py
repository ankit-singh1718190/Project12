from django.contrib import admin
from .models import StudentModel
@admin.register(StudentModel)
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','city']