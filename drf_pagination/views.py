from django.shortcuts import render
from drf_pagination.serializers import StudentSerializer


from rest_framework import viewsets
from rest_framework.authentication import (
    BasicAuthentication,
)
from rest_framework.permissions import (
    IsAuthenticated,
)

'''
Ways by which paginationa can be applied 

1. Using global settings 

2. Using Pagination Perview
'''

# Applying pagination based on views 

class ThrottlingStudents(viewsets.ModelViewSet):
    queryset = StudentSerializer.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
