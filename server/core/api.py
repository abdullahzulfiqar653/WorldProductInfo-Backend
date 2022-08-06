from django.urls import path
from core.views import *


urlpatterns = [
    path('category/', CategoryListView.as_view()),      # done
    path('category/filter/name/', CategoryFilterNameView.as_view()),  # done
    path('product/type/filter/name/', ProductTypeFilterNames.as_view()),  # done
    path('manufacturer/filter/name/', ManufacturerFilter.as_view()),     # done

    # Below endpoints are ready but still in testing
    path('products/', ProductListView.as_view()),  
    # path('product/attribute/filter/name/',
    #      ProductAttribuiteFilterNames.as_view()),
]
