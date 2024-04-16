from django.contrib import admin
from login.models import Person, Student, PosGradStudent, Professional

admin.site.register(Person)
admin.site.register(Student)
admin.site.register(PosGradStudent)
admin.site.register(Professional)
