from django.db import models
from django.conf import settings
from courses.models import Course

class Payment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    chapa_tx_ref = models.CharField(max_length=100, unique=True)
    chapa_order_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("success", "Success"), ("failed", "Failed")],
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, default="telebirr")  # e.g., telebirr, mpesa, cbebirr

    def __str__(self):
        return f"{self.student.username} - {self.course.title} - {self.status}"