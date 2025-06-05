from django.contrib import admin
from .models import Category, Course, Lesson

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    search_fields = ('title', 'instructor__username', 'category__name')
    list_filter = ('category', 'language')

admin.site.register(Course, CourseAdmin)
admin.site.register(Category)
admin.site.register(Lesson)
