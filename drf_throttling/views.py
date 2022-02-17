from django.shortcuts import render
from drf_throttling.custom_throttle import CustomThrottle

from drf_throttling.models import Students
from drf_throttling.serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework.generics import(
    CreateAPIView,
    DestroyAPIView,

    RetrieveAPIView,
    UpdateAPIView,
    ListAPIView,

)
from rest_framework.authentication import (
    BasicAuthentication,

)
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.throttling import (
    AnonRateThrottle,
    ScopedRateThrottle,
    UserRateThrottle,
    SimpleRateThrottle,
    BaseThrottle,
)

# Create your views here.
'''
Applying throttling on 
1.Anonymous User
2.Autheticated User
3.Custom class 
'''
class ThrottlingStudents(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    throttle_classes= [AnonRateThrottle,CustomThrottle]


'''
Appling throlling on various parts of apis
'''
class StudentList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'list'

class StudentCreate(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'create'



class StudentUpdate(UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'update'



class StudentDestroy(DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'destroy'



class StudentRetrieve(RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'retrieve'




