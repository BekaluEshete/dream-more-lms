from django.db import models
from users.models import User
from courses.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"
    class Meta:
        unique_together = ('student', 'course')  # Ensures unique student-course pair