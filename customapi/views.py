import json
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from customapi.serializers import Student, StudentSerializers
# Create your views here.

@api_view()
def users(request):
    context =[
        {
            'name' : 'shubham',
            'phone' : '8800531462',
            'customer' : 'name'
        }
        
    ]
    return Response(json.dumps(context)) 

@api_view()
def single_object(request):
    student1 = Student('shubham kumar mishra' ,409,100)
    response = StudentSerializers(student1)
    return Response(response.data)

@api_view()
def multiple_objects(request):
    student1 = Student('shubham kumar mishra' ,409,100)
    student2 = Student('jatin' ,406,99)
    student3 = Student('udit' ,410,98)
    student4 = Student('sujit' ,70,89)
    response = StudentSerializers([student1,student2, student3, student4],many=True)
    return Response(response.data)







    