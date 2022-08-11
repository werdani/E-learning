from ast import Delete
from review.models import Review
from review.api.serializers import ReviewSerlizer
from rest_framework import generics

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .permissions import IstheUser

# -------------------create--view------------------------
class ReviewAPIListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerlizer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
# -------------------update single review--delete review------------------------
# Retrieve---Show
# Destroy---Delete
# Update---Update
class SingleReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IstheUser]
    serializer_class = ReviewSerlizer
    queryset = Review.objects.all()
    lookup_url_kwarg = 'id'
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


