from rest_framework import serializers

from queryapi.models import Student
# Create your serializers here.

class StudentSerializer(serializers.Serializer):
    roll = serializers.IntegerField()
    name = serializers.CharField()
    # class Meta:
    #     model = Student
    #     fields = ('name', 'roll')
    #     extra_kwargs = {'roll': {'read_only': False}}