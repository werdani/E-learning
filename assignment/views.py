from django.shortcuts import render
from .models import Assignment
from rest_framework.decorators import api_view
from .serializers import AssignmentSerializer
from rest_framework import status, filters
from rest_framework.response import Response

# Create your views here.
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.viewsets import ReadOnlyModelViewSet


# class AssignmentViewSet(ReadOnlyModelViewSet):
#     queryset = Assignment.objects.all()
#     serializer_class = AssignmentSerializer
    # permission_classes = [IsAuthenticated]

@api_view(['GET','POST'])
def Assign_List(request):
    if request.method == 'GET':
        assigment = Assignment.objects.all()
        serializer = AssignmentSerializer(assigment, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
