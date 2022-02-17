from rest_framework import serializers

from drf_auth_perm.models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields =  ['id','name','roll','branch']