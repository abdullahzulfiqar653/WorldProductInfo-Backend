from django.urls import path
from core.views import *


urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/filter/name/', CategoryFilterNameView.as_view()),
    path('manufacturer/filter/name/', ManufacturerFilter.as_view()),
    path('product/type/filter/name/', ProductTypeFilterNames.as_view()),
    path('product/attribute/filter/name/',
         ProductAttribuiteFilterNames.as_view()),
]
