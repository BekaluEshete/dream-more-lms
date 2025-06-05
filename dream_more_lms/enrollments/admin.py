from django.contrib import admin
from .models import Enrollment

# Register your models here.

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_on', 'progress')
    list_filter = ('course', 'student')

admin.site.register(Enrollment, EnrollmentAdmin) 
 
