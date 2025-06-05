from rest_framework import serializers
from .models import Category, Course,Lesson


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class CourseLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField()
    category = CourseCategorySerializer(read_only=True)
    lessons = CourseLessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
