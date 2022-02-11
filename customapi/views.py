from calendar import c
from http.client import HTTPResponse
import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
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