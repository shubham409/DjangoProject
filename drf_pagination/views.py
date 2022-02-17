from django.shortcuts import render
from drf_pagination.models import Students
from drf_pagination.serializers import StudentSerializer


from rest_framework import viewsets
from rest_framework.authentication import (
    BasicAuthentication,
)
from rest_framework.permissions import (
    IsAuthenticated,
)
from drf_pagination.custom_pagination import CustomPagination
'''
Ways by which paginationa can be applied 

1. Using global settings 

2. Using Pagination Perview
'''


class PaginationStudents(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

# Applying pagination based on views 
class SpecificViewPaginationStudents(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    pagination_class= CustomPagination
