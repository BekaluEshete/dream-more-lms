from django.contrib import admin
from .models import Discussion, Reply

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'question', 'created_at')
    list_filter = ('course', 'created_at')

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('discussion', 'user', 'reply_text', 'created_at')
    list_filter = ('discussion', 'created_at')
