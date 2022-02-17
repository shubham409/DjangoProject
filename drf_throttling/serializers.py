from rest_framework import serializers

from drf_throttling.models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields =  ['id','name','roll','branch']