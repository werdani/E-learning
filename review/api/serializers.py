from rest_framework import serializers
from review.models import Review

class ReviewSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
