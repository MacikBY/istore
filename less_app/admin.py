from django.contrib import admin

from less_app.models import LessUser, Hobby, School, Student, Course

# Register your models here.
admin.site.register(LessUser)
admin.site.register(Hobby)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Course)