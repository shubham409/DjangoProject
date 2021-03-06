from django.shortcuts import render
from drf_auth_perm.models import Students
from drf_auth_perm.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import (
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    DjangoModelPermissionsOrAnonReadOnly
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Create your views here.
from rest_framework.response import Response
from drf_auth_perm.custom_permissions import CustomPermissionOnlyStaff, CustomPermissionOnlySuperUser
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


# class AllStudentsModelViewSet(viewsets.ModelViewSet):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
#     # authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]    

# class ReadonlyStudentsModelViewSet(viewsets.ModelViewSet):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [ DjangoModelPermissionsOrAnonReadOnly]  

# class StaffStudentsModelViewSet(viewsets.ModelViewSet):
#     # only for staff users that is admin and staff simple users cant use this
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAdminUser]  

# -------------------------------------------------------------------
'''
For token Validation we have to First create Token.
Tokens can be generated by following ways :- 

1. go to Admin and click token select user for getting token for that user(it comes in admin panel because we add rest_framework.authtoken in installed apps in settings.py)
    or
2. use command 
    python manage.py drf_create_token username_without_any_quotes
EX. 
    python manage.py drf_create_token Admin

3. by exposing API for getting token Using Following code 
    from rest_framework.authtoken.views import obtain_auth_token
    urlpatterns = [
        path('gettoken',obtain_auth_token)
    ]

    Send a Post request With Json Body of user name and password and get token
EX.
    Post Request 
    {
        "username": "simple",
        "password": "@password123"
    }
    Respose
    {
        "token": "2f3ab608fa8bb1f0910dca1b57bebd09877324c1"
    }
    Act as Get if Token Exists as well as Create when token doesn't exists

4. use custom class for getting token
'''


class TokenStudentModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    authentication_classes =[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    

class GetCustomToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer =   self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        data = {'token':token.key,'user':user.username}
        return Response(data)

# -------------------------------------------------------------------------
# 

class OnlyStaffStudentModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [CustomPermissionOnlyStaff]

class OnlySuperusertudentModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [CustomPermissionOnlySuperUser]