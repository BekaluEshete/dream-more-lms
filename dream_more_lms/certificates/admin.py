from django.contrib import admin
from django.utils.html import format_html
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display  = ['id', 'student', 'course', 'issued_date', 'download']
    list_filter   = ['course', 'issued_date']
    search_fields = ['student__username', 'course__title']

    def download(self, obj):
        if obj.certificate_file:
            return format_html(
                '<a href="{}" target="_blank">PDF</a>',
                obj.certificate_file.url
            )
        return '-'
    download.short_description = 'Certificate'
