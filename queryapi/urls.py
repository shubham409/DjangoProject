from django.contrib import admin
from django.urls import path , include

from queryapi.views import GetAllStudents, GetStudentWithRollUsingKeyword,GetStudentWithRoll

urlpatterns = [

    path('all/',GetAllStudents.as_view()),
    path('get/<int:roll>',GetStudentWithRollUsingKeyword.as_view()),
    path('get/',GetStudentWithRoll.as_view())
    
]
