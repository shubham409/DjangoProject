from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination,
)

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_query_param= 'p'
    # for giving client fliexibility to change number of values perpage 
    page_size_query_param= 'records'
    # restrict max vaues that can be asked to avoid server slowdown
    max_page_size = 6
    # string to go to last page 
    last_page_strings = 'end'

class CustomLimitOffsetPagination(PageNumberPagination):
    default_limit = 7
    page_query_param= 'p'
    page_size_query_param= 'records'
    max_page_size = 6
    last_page_string = 'end'


# only with the model with a mandatory field created(time stamp field ) if we dont have created field we can override this behaviour
# can only go forward and backwards , doesn't support going to any page number
class CustomCursorPagination(PageNumberPagination):
    page_size = 3
    # overriding created field
    odering= 'id'
    cursor_query_param= 'cursor_name'



