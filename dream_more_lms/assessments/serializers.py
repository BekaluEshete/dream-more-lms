from rest_framework import serializers
from .models import Quiz, Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True, source='answer_set')

    class Meta:
        model = Question
        fields = ['id', 'quiz', 'text', 'answers']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True, source='question_set')

    class Meta:
        model = Quiz
        fields = ['id', 'course', 'title', 'created_at', 'questions']
