from django.urls import path
from core.views import *


urlpatterns = [
    path('category/', CategoryListView.as_view()),      # done
    path('category/filter/name/', CategoryFilterNameView.as_view()),  # done
    path('product/type/filter/name/', ProductTypeFilterNames.as_view()),  # done
    path('manufacturer/filter/name/', ManufacturerFilter.as_view()),     # done

    # Below endpoints are ready but still in testing
    path('products/', ProductListView.as_view()),  # done
    path('product/type/list/', ProductTypeFilterListView.as_view()),     # Done
    path('product/manufacturer/filter/',
         ProductManufacterFilterListView.as_view()),  # Done
    path('products/search/', SearchProductListView.as_view()),  # Done
    # path('product/attribute/filter/name/',
    #      ProductAttribuiteFilterNames.as_view()),
]
