from django.shortcuts import render
from drf_auth_perm.models import Students
from drf_auth_perm.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import (
    BasicAuthentication,
)
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    DjangoModelPermissionsOrAnonReadOnly
    
)
# Create your views here.

'''
following are some authentications and permissions

authentication.BaseAuthentication
authentication.BasicAuthentication
authentication.SessionAuthentication
authentication.TokenAuthentication
authentication.RemoteUserAuthentication


permissions.AllowAny
permissions.BasePermission
permissions.IsAdminUser
permissions.IsAuthenticated
permissions.IsAuthenticatedOrReadOnly
'''


class AllStudentsModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]    

class ReadonlyStudentsModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [ DjangoModelPermissionsOrAnonReadOnly]  

class StaffStudentsModelViewSet(viewsets.ModelViewSet):
    # only for staff users that is admin and staff simple users cant use this
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]  


