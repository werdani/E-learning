from rest_framework import serializers
from .models import Category

# Category Serializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['cat_name']


class AllCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
<<<<<<< HEAD
        fields = ['id', 'cat_name']
=======
        fields = ['pk', 'cat_name']
>>>>>>> cce6dda622ac49ffca6c75bd728a20c71d57f42d
