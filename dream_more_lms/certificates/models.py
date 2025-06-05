from io import BytesIO
from datetime import datetime

from django.db import models
from django.core.files.base import ContentFile
from django.conf import settings

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

from users.models import User
from courses.models import Course


class Certificate(models.Model):
    student          = models.ForeignKey(User,    on_delete=models.CASCADE)
    course           = models.ForeignKey(Course,  on_delete=models.CASCADE)
    issued_date      = models.DateTimeField(auto_now_add=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True)

    def __str__(self):
        return f'Certificate • {self.student} • {self.course}'

    # ---  AUTO-GENERATE PDF ---------------------------------------------------
    def save(self, *args, **kwargs):
        creating = self._state.adding          # True only on first save

        super().save(*args, **kwargs)          # save first (we need PK)

        if creating and not self.certificate_file:
            pdf_bytes = self._build_pdf()      # create PDF in memory
            filename  = f'certificate_{self.pk}.pdf'
            self.certificate_file.save(filename, ContentFile(pdf_bytes), save=False)
            super().save(update_fields=['certificate_file'])  # save path only

    def _build_pdf(self) -> bytes:
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        # --- simple styling ---------------------------------------------------
        c.setFont('Helvetica-Bold', 24)
        c.drawCentredString(width / 2, height - 6*cm, 'Certificate of Completion')

        c.setFont('Helvetica', 14)
        c.drawCentredString(width / 2, height - 8*cm,
                            f'This certifies that')

        c.setFont('Helvetica-Bold', 18)
        c.drawCentredString(width / 2, height - 10*cm,
                            self.student.get_full_name() or self.student.username)

        c.setFont('Helvetica', 14)
        c.drawCentredString(width / 2, height - 12*cm,
                            f'has successfully completed the course')

        c.setFont('Helvetica-Bold', 16)
        c.drawCentredString(width / 2, height - 14*cm, self.course.title)

        date_str = self.issued_date.strftime('%B %d, %Y')
        c.setFont('Helvetica', 12)
        c.drawCentredString(width / 2, height - 17*cm, f'Date of Issue : {date_str}')

        # signature line (optional)
        c.line(width/2 - 3*cm, height - 20*cm, width/2 + 3*cm, height - 20*cm)
        c.drawCentredString(width / 2, height - 21*cm, 'Instructor')

        c.showPage()
        c.save()
        buffer.seek(0)
        return buffer.getvalue()
