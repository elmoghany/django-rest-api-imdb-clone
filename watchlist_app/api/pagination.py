from rest_framework import pagination

class WatchListPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'page_number'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'
    
class WatchListLimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'
    
class WatchListCursorPagination(pagination.CursorPagination):
    page_size = 5
    