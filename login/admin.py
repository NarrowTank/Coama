from django.contrib import admin
from login.models import Person, Student, PosGradStudent, Professional

class PersonAdmin(admin.ModelAdmin):
    list_display = ["id_name", "email", "phone", "is_deficient", "payed", "date_added"]
    date_hierarchy = "date_added"

admin.site.register(Person, PersonAdmin)
admin.site.register(Student)
admin.site.register(PosGradStudent)
admin.site.register(Professional)
