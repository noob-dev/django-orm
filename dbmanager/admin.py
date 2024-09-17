from django.contrib import admin
from .models import Faculty, Group, Student, Kafedra, Subject, Teacher

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faculty')
    search_fields = ('name',)
    list_filter = ('faculty',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'kafedra', 'group')
    search_fields = ('first_name', 'last_name')
    list_filter = ('kafedra', 'group')

@admin.register(Kafedra)
class KafedraAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'kafedra')
    search_fields = ('name',)
    list_filter = ('kafedra',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'subject')
    search_fields = ('first_name', 'last_name')
    list_filter = ('subject',)
