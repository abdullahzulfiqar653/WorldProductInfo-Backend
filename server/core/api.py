from django.urls import path
from core.views import *


urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/filter/name/', CategoryFilterNameView.as_view()),
    path('product/type/filter/name/', ProductTypeFilterNames.as_view()),
]
