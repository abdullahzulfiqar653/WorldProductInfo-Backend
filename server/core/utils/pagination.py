from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class PageNumberPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_size = 10
    max_page_size = 50


class LimitOffsetPagination(LimitOffsetPagination):
    default_limit = 12
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 51
