from django.urls import path
from . import views

urlpatterns = [
    path('quizzes/', views.quiz_list, name='quiz-list'),
    path('quizzes/<int:pk>/', views.quiz_detail, name='quiz-detail'),
    path('questions/', views.question_list, name='question-list'),
    path('answers/', views.answer_list, name='answer-list'),
]
