from django.contrib import admin
from django.urls import path , include

from queryapi.views import (
    GetAllStudents, 
    GetStudentWithRollUsingKeyword,
    GetStudentWithRoll,
    FilterNameStartsWith,

    FilterContains,
    FilterIn,
    CreateStudent,
    AggregateCount,
    AggregateSum,
    StartsWithOrGreaterThan,
    StartsWithAndGreaterThan,
    OrderBy,
)

urlpatterns = [

    path('all/',GetAllStudents.as_view()),
    path('get/<int:roll>',GetStudentWithRollUsingKeyword.as_view()),
    path('get/',GetStudentWithRoll.as_view()),
    path('filter/',FilterNameStartsWith.as_view()),
    # -----------------------
    path('contains/',FilterContains.as_view()),
    path('in/',FilterIn.as_view()),
    path('create/',CreateStudent.as_view()),
    # -----------------------------------------
    path('count/',AggregateCount.as_view()),
    path('sum/',AggregateSum.as_view()),
    # -----------------------------------
    path('or/',StartsWithOrGreaterThan.as_view()),
    path('and/',StartsWithAndGreaterThan.as_view()),
    # ------------------------------------
    path('orderby/',OrderBy.as_view()),

]
