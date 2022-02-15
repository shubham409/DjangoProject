from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from queryapi.custom_functions import give_error, give_message, success_message
from queryapi.serializers import StudentSerializer
from queryapi.models import Student
import json
from django.db.models import Count , Max,Min,Avg,Sum
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
    

# ----------------------------------------------------------------------

class FilterContains(APIView):

    def get(self, request , format=None):
        contains = request.GET.get('contains')
        return self.filter_contains(contains)

    def post(self, request , format=None):
        contains = request.POST.get('contains')
        return self.filter_contains(contains)

    def valid_filter(self,contains :str ):
        try:
            val=Student.objects.filter(name__contains=contains)
            return val
        except:
            return None

    def filter_contains(self,contains):
        result = self.valid_filter(contains)
        if result is not None :
            serializer = StudentSerializer(result,many=True)
            return Response(serializer.data)
        else:
            message = "Please enter Correct String"
            return Response(give_error(message))


class FilterIn(APIView):

    def get(self, request , format=None):
        json_object = json.loads(request.body)
        iter = json_object.get('iter')
        return self.filter_in(iter)

    def post(self, request , format=None):
        json_object = json.loads(request.body)
        iter = json_object.get('iter')
        return self.filter_in(iter)

    def valid_filter(self,iter :str ):
        try:
            val=Student.objects.filter(roll__in=iter)
            return val
        except:
            return None

    def filter_in(self,iter):
        result = self.valid_filter(iter)
        if result is not None :
            serializer = StudentSerializer(result,many=True)
            return Response(serializer.data)
        else:
            message = "Please enter Correct String"
            return Response(give_error(message))


class OrderBy(APIView):

    def get(self, request , format=None):
        print(request.GET)
        orderby = request.GET.get('orderby')
        print(orderby)
        field = request.GET.get('field')
        print(field)
        return self.order_by(orderby , field)

    def post(self, request , format=None):
        field = request.POST.get('field')
        orderby = request.POST.get('orderby')
        return self.order_by(orderby , field)

    def valid_orderby(self, orderby :str, field_name:str):
        try:
            field =None
            if orderby=='inc':
                field = field_name
            elif orderby=='dec':
                field= '-'+field_name
            else:
                field = '?'
            print(field)
            val=Student.objects.order_by(field)
            return val
        except Exception as e:
            print(e)
            return None

    def order_by(self,orderby,field_name):
        result = self.valid_orderby(orderby,field_name)
        if result is not None :
            serializer = StudentSerializer(result,many=True)
            return Response(serializer.data)
        else:
            message = "Please enter valid query "
            return Response(give_error(message))
# -------------------------------------------------------------

class CreateStudent(APIView):

    def get(self, request , format=None):
        json_object = json.loads(request.body)
        student = json_object.get('student')
        print(student)
        return self.create_student(student)

    def post(self, request , format=None):
        json_object = json.loads(request.body)
        student = json_object.get('student')
        print(student)
        return self.create_student(student)

    def valid_create(self,student :str ):
        try:
            name = student.get("name")
            roll = student.get("roll")
            if(name is not None and roll is not None):
                val=Student.objects.create(name = name , roll= roll)
                return val
            else:
                return None
        except Exception as e:
            print(e)
            return None

    def create_student(self,student):
        result = self.valid_create(student)
        print(result)
        if result is not None :
            message = f'{result} has been saved'
            return Response(success_message(message))
        else:
            message = "Please enter Student with different roll no."
            return Response(give_error(message))
# ----------------------------------------------------------
# Aggregate

class AggregateCount(APIView):

    def get(self, request , format=None):
        return self.aggregate_count()

    def post(self, request , format=None):
        return self.aggregate_count()

    def valid_count(self ):
        try:
            val=Student.objects.aggregate(Count('roll'))
            return val

        except Exception as e:
            print(e)
            return None

    def aggregate_count(self):
        result = self.valid_count()
        print(result)
        if result is not None :
            message = f'count of the record is {result.get("roll__count")} '
            return Response(success_message(message))
        else:
            message = "Please make valid request"
            return Response(give_error(message))
 

class AggregateSum(APIView):

    def get(self, request , format=None):
        return self.aggregate_Sum()

    def post(self, request , format=None):
        return self.aggregate_Sum()

    def valid_Sum(self ):
        try:
            val=Student.objects.aggregate(Sum('roll'))
            return val

        except Exception as e:
            print(e)
            return None

    def aggregate_Sum(self):
        result = self.valid_Sum()
        print(result)
        if result is not None :
            message = f'sum of the roll numbers is {result.get("roll__sum")} '
            return Response(success_message(message))
        else:
            message = "Please make valid request"
            return Response(give_error(message))
# -----------------------------------------------------------
# Or
class StartsWithOrGreaterThan(APIView):

    def get(self, request , format=None):
        start_with = request.GET.get('startswith')
        start_with_result = self.valid_startswith(start_with)
        greater_than = request.GET.get('greaterthan')
        greater_than_result = self.valid_greaterthan(greater_than)
        return self.or_query(start_with_result,greater_than_result)


    def post(self, request , format=None):
        print(request.POST)
        start_with = request.POST.get('startswith')
        start_with_result = self.valid_startswith(start_with)
        greater_than = request.POST.get('greaterthan')
        greater_than_result = self.valid_greaterthan(greater_than)
        return self.or_query(start_with_result,greater_than_result)

    def or_query(self,start_with_result, greater_than_result):
        if start_with_result is not None and greater_than_result is not None:
            result = start_with_result | greater_than_result
            serializer = StudentSerializer(result,many=True)
            return Response(serializer.data)
        else:
            message = "Please enter valid query"
            return Response(give_error(message))

    def valid_greaterthan(self,value :str ):
        try:
            val=Student.objects.filter(roll__gte=value)
            return val
        except Exception as e :
            print(e)
            return None

    def valid_startswith(self,start_with :str ):
        try:
            val=Student.objects.filter(name__startswith=start_with)
            return val
        except Exception as e :
            print(e)
            return None

class StartsWithAndGreaterThan(APIView):

    def get(self, request , format=None):
        start_with = request.GET.get('startswith')
        start_with_result = self.valid_startswith(start_with)
        greater_than = request.GET.get('greaterthan')
        greater_than_result = self.valid_greaterthan(greater_than)
        return self.and_query(start_with_result,greater_than_result)

    def post(self, request , format=None):
        print(request.POST)
        start_with = request.POST.get('startswith')
        start_with_result = self.valid_startswith(start_with)
        greater_than = request.POST.get('greaterthan')
        greater_than_result = self.valid_greaterthan(greater_than)
        return self.and_query(start_with_result,greater_than_result)

    def and_query(self,start_with_result, greater_than_result):
        if start_with_result is not None and greater_than_result is not None:
            result = start_with_result & greater_than_result
            serializer = StudentSerializer(result,many=True)
            return Response(serializer.data)
        else:
            message = "Please enter valid query"
            return Response(give_error(message))

    def valid_greaterthan(self,value :str ):
        try:
            val=Student.objects.filter(roll__gte=value)
            return val
        except Exception as e :
            print(e)
            return None

    def valid_startswith(self,start_with :str ):
        try:
            val=Student.objects.filter(name__startswith=start_with)
            return val
        except Exception as e :
            print(e)
            return None
            