from rest_framework import pagination

class WatchListPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'page_number'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'