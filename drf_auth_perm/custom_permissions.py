from drf_auth_perm.models import Students
from drf_auth_perm.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import (
    BasicAuthentication,
    TokenAuthentication,
    BaseAuthentication,
)
from rest_framework.authtoken.models import Token
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    DjangoModelPermissionsOrAnonReadOnly,
    BasePermission,
    
)
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Create your views here.
from rest_framework.response import Response

class CustomPermissionOnlyStaff(BasePermission):
    message = 'Sorry You are not Staff Member !!'

    def has_permission(self, request, view):
        if request.method == 'POST':
            data = request.data
            current_user = data.get('username')
            user = User.objects.get(username=current_user)
            return user.is_staff
        return False
    # def has_object_permission(self, request, view, obj):
    #     return True


class CustomPermissionOnlySuperUser(BasePermission):
    message = 'Sorry You are not Super User !!'
    def has_permission(self, request, view):
        if request.method == 'POST':
            data = request.data
            current_user = data.get('username')
            user = User.objects.get(username=current_user)
            user.is_superuser
        return False
