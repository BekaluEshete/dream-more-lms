from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# QUIZZES
@swagger_auto_schema(
    method='GET',
    responses={
        200: QuizSerializer(many=True),
    }
)
@swagger_auto_schema(
    method='POST',
    request_body=QuizSerializer,
    responses={
        201: QuizSerializer,
        400: openapi.Response('Bad Request', examples={'application/json': {'error': 'Invalid data'}})
    }
)
@api_view(['GET', 'POST'])
def quiz_list(request):
    if request.method == 'GET':
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='GET',
    responses={
        200: QuizSerializer,
        404: openapi.Response('Not Found', examples={'application/json': {'error': 'Quiz not found'}})
    }
)
@swagger_auto_schema(
    method='PUT',
    request_body=QuizSerializer,
    responses={
        200: QuizSerializer,
        400: openapi.Response('Bad Request'),
        404: openapi.Response('Not Found')
    }
)
@swagger_auto_schema(
    method='DELETE',
    responses={
        204: openapi.Response('No Content'),
        404: openapi.Response('Not Found')
    }
)
@api_view(['GET', 'PUT', 'DELETE'])
def quiz_detail(request, pk):
    try:
        quiz = Quiz.objects.get(pk=pk)
    except Quiz.DoesNotExist:
        return Response({'error': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = QuizSerializer(quiz, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        quiz.delete()
        return Response({'message': 'Quiz deleted'}, status=status.HTTP_204_NO_CONTENT)

# QUESTIONS
@swagger_auto_schema(
    method='GET',
    responses={
        200: QuestionSerializer(many=True),
    }
)
@swagger_auto_schema(
    method='POST',
    request_body=QuestionSerializer,
    responses={
        201: QuestionSerializer,
        400: openapi.Response('Bad Request', examples={'application/json': {'error': 'Invalid data'}})
    }
)
@api_view(['GET', 'POST'])
def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ANSWERS
@swagger_auto_schema(
    method='GET',
    responses={
        200: AnswerSerializer(many=True),
    }
)
@swagger_auto_schema(
    method='POST',
    request_body=AnswerSerializer,
    responses={
        201: AnswerSerializer,
        400: openapi.Response('Bad Request', examples={'application/json': {'error': 'Invalid data'}})
    }
)
@api_view(['GET', 'POST'])
def answer_list(request):
    if request.method == 'GET':
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)