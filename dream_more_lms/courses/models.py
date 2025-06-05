from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    language = models.CharField(max_length=20, choices=(("en", "English"), ("am", "Amharic")))
    instructor = models.ForeignKey(User, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Lesson(models.Model):# to made the model non editable make the  editable False
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True)
    pdf = models.FileField(upload_to='lessons/', blank=True)
    order = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.title} - {self.course.title}"

