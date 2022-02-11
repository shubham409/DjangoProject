from rest_framework import serializers


# suppose we have this class and we want json value of it to return so we create serealizers

#class 
class Student():
    def __init__(self,name,roll,marks) -> None:
        self.name = name 
        self.roll = roll
        self.marks = marks

# serializers of class above it 
class StudentSerializers(serializers.Serializer):
    name = serializers.CharField()
    roll = serializers.IntegerField()
    marks = serializers.IntegerField()
