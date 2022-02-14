from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from queryapi.serializers import StudentSerializer
from queryapi.models import Student

# Create your views here.
class GetAllStudents(APIView):
    def get(self, request , format=None):
        query_set = Student.objects.all()
        serializer = StudentSerializer(query_set ,many=True)
        return Response(serializer.data)
    def post(self, request , format=None):
        query_set = Student.objects.all()
        serializer = StudentSerializer(query_set ,many=True)
        return Response(serializer.data)

class GetStudentWithRollUsingKeyword(APIView):

    def get(self, request , format=None,**kwargs):
        roll_no = kwargs.get('roll')
        if self.valid_get(roll_no) :
            result = Student.objects.get(roll=roll_no)
            serializer = StudentSerializer(result)
            return Response(serializer.data)
        else:
            error = {
                'error':'please enter valid roll'
            }
            return Response(error)

    def valid_get(self,roll_no :int ):
        try:
            Student.objects.get(roll=roll_no)
            return True
        except:
            return False

class GetStudentWithRoll(APIView):
    def get(self, request , format=None):
        print(request)
        print(request.GET)
        roll_no = request.GET.get('roll')
        if self.valid_get(roll_no) :
            result = Student.objects.get(roll=roll_no)
            serializer = StudentSerializer(result)
            return Response(serializer.data)
        else:
            error = {
                'error':'please enter valid roll'
            }
            return Response(error)


    def post(self, request , format=None):
        print(request.POST)
        roll_no = request.POST.get('roll')
        print(type(roll_no))
        if self.valid_get(roll_no) :
            result = Student.objects.get(roll=roll_no)
            serializer = StudentSerializer(result)
            return Response(serializer.data)
        else:
            error = {
                'error':'please enter valid roll'
            }
            return Response(error)  

    def valid_get(self,roll_no :int ):
        try:
            Student.objects.get(roll=roll_no)
            return True
        except:
            return False


