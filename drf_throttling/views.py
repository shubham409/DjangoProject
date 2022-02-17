from django.shortcuts import render

from drf_throttling.models import Students
from drf_throttling.serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework.authentication import (
    BasicAuthentication,
)
from rest_framework.permissions import (
    IsAuthenticated,
)


# Create your views here.
class ThrottlingStudents(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]