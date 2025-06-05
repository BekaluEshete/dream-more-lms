from rest_framework import serializers
from .models import Certificate

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Certificate
        fields = ['id', 'student', 'course', 'issued_date', 'certificate_file']
        read_only_fields = ['issued_date', 'certificate_file']
