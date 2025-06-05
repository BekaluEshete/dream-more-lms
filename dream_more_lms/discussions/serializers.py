from rest_framework import serializers
from .models import Discussion, Reply

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
        read_only_fields = ['created_at', 'user']

class DiscussionSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Discussion
        fields = '__all__'
        read_only_fields = ['created_at', 'user']
