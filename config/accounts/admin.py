from django.contrib import admin

from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'department', 'year')
    search_fields = ('username', 'email', 'department')
    
