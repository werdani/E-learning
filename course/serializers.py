from rest_framework import serializers
from course.models import Category, Course
# from category.serializers import Categoryerializer
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name','course_instructor','course_description','course_image','course_category']
        

class Course_all_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','course_name','course_instructor','course_description','course_image','course_category']