from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from queryapi.custom_functions import give_error
from queryapi.serializers import StudentSerializer
from queryapi.models import Student

# Create your views here.
'''
Model.objects.

list of all the query methods present in orm 
Model.objects.all()
Model.objects.get(key=value)
Model.objects.filter()
Model.objects.exclude()
Model.objects.order_by('field')
Model.objects.order_by('-field')
Model.objects.order_by('?')
Model.objects.order_by().reverse
Model.objects.all()[form:to]
Model.objects.values()
Model.objects.value_list()
'''
'''
Field lookups these are used with get(), filter() , exclude().
Chaining is also possible with lookups.
Model.objects.filter(field__exact     = value)
Model.objects.filter(field__iexact    = value)
Model.objects.filter(field__contains  = value)
Model.objects.filter(field__icontains = value)
Model.objects.filter(field__in  = iterables)
Model.objects.filter(field__gt  = value)
Model.objects.filter(field__gte = value)
Model.objects.filter(field__lt  = value)
Model.objects.filter(field__lte = value)
Model.objects.filter(field__startswith  = value)
Model.objects.filter(field__istartswith = value)
Model.objects.filter(field__endswith  =  value)
Model.objects.filter(field__iendswith =  value)
Model.objects.filter(field__range = (start, end))
Model.objects.filter(field__date = datetime.date(year,month,day))
Model.objects.filter(field__date__gt = datetime.date(year,month,day))
Model.objects.filter(field__year = year)
Model.objects.filter(field__year__gt = year)
Model.objects.filter(field__month = month)
Model.objects.filter(field__month__gte = month)
Model.objects.filter(field__day = day)
Model.objects.filter(field__day__gt = day)
Model.objects.filter(field__week = 1 to 53)
Model.objects.filter(field__week__lt = 1 to 53)
Model.objects.filter(field__week__day)
Model.objects.filter(field__quarter = 1 to 4)
Model.objects.filter(field__time = datetime.time(minute,second))
Model.objects.filter(field__time__range = (datetime.time(minute,second),datetime.time(minute,second)))
Model.objects.filter(field__hour   = 0 to 23)
Model.objects.filter(field__minute = 0 to 59)
Model.objects.filter(field__second = 0 to 59)
Model.objects.filter(field__isnull = True or False)
Model.objects.filter(field__regex  = r'python regex')
Model.objects.filter(field__iregex = r'python regex')
'''
'''
Aggregate functions
Avg
Count
Max
Min
StdDev
Sum
Variance
'''
''''
And and Or operator
Using OR
Model.objects.filter(key = value) | Model.objects.filter(key = value) 
            or 
from db.models import Q
Model.objects.filter( Q(key = value) | Q(key = value) )

Using And 
Model.objects.filter(key = value) & Model.objects.filter(key = value) 
            or 
from db.models import Q
Model.objects.filter( Q(key = value) & Q(key = value) )
            or 
Model.objects.filter(key = value ,key = value)

'''


# For getting all the students using get or post method 
class GetAllStudents(APIView):
    def get(self, request , format=None):
        query_set = Student.objects.all()
        serializer = StudentSerializer(query_set ,many=True)
        return Response(serializer.data)
    def post(self, request , format=None):
        query_set = Student.objects.all()
        serializer = StudentSerializer(query_set ,many=True)
        return Response(serializer.data)

 
# For getting about the students which have been passed in url after /(farword slash)
# works for only get 
class GetStudentWithRollUsingKeyword(APIView):
    def get(self, request , format=None,**kwargs):
        roll_no = kwargs.get('roll')
        result = self.valid_get(roll_no)
        if result is not None:
            serializer = StudentSerializer(result)
            return Response(serializer.data)
        else:
            error = 'please enter valid roll'
            return Response(give_error(error))

    def valid_get(self,roll_no :int ):
        try:
            val = Student.objects.get(roll=roll_no)
            return val
        except:
            return None

# give Student for which roll no. is given 
# Works for both get and post 
class GetStudentWithRoll(APIView):
    def get(self, request , format=None):
        roll_no = request.GET.get('roll')
        return self.get_roll(roll_no)

    def post(self, request , format=None):
        roll_no = request.POST.get('roll')
        return self.get_roll(roll_no) 

    def valid_get(self,roll_no :int ):
        try:
            val = Student.objects.get(roll=roll_no)
            return val
        except:
            return None
    
    def get_roll(self,roll_no):
        result = self.valid_get(roll_no)
        print(result)
        if  result is not None:
            serializer = StudentSerializer(result)
            return Response(serializer.data)
        else:
            error='please enter valid roll'
            return Response(give_error(error))       

# returns query set for which name start with given string 
# working on post and get
class FilterNameStartsWith(APIView):

    def get(self, request , format=None):
        print(request)
        print('inside get method = ',request.GET)
        start_with = request.GET.get('startswith')
        if self.valid_filter(start_with) :
            result = Student.objects.filter(name__startswith=start_with)
            serializer = StudentSerializer(result,many=True)
            return Response(serializer.data)
        else:
            error = {
                'error':'Please Enter Valid String To Use Filter Starts With'
            }
            return Response(error)


    def post(self, request , format=None):
        print(request.POST)
        start_with = request.POST.get('startswith')
        if self.valid_filter(start_with) :
            result = Student.objects.filter(name__startswith=start_with)
            serializer = StudentSerializer(result,many=True)
            return Response(serializer.data)
        else:
            error = {
                'error':'Please Enter Valid String To Use Filter Starts With'
            }
            return Response(error)

    def valid_filter(self,start_with :str ):
        try:
            Student.objects.filter(name__startswith=start_with)
            return True
        except:
            return False


class FilterNameStartsWith(APIView):

    def get(self, request , format=None):
        start_with = request.GET.get('startswith')
        return self.filter_startswith(start_with)

    def post(self, request , format=None):
        start_with = request.POST.get('startswith')
        return self.filter_startswith(start_with)

    def valid_filter(self,start_with :str ):
        try:
            val=Student.objects.filter(name__startswith=start_with)
            return val
        except:
            return None

    def filter_startswith(self,start_with):
        result = self.valid_filter(start_with)
        if result is not None :
            serializer = StudentSerializer(result,many=True)
            return Response(serializer.data)
        else:
            message = "Please enter Correct String"
            return Response(give_error(message))
    

