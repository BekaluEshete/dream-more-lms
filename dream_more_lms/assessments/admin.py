from django.contrib import admin
from .models import Quiz, Question, Answer

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'course', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['title', 'course__title']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'quiz']
    list_filter = ['quiz']
    search_fields = ['text', 'quiz__title']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'question', 'is_correct']
    list_filter = ['is_correct', 'question']
    search_fields = ['text', 'question__text']
