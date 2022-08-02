from django.urls import path, include
from core.views.product_views import *

urlpatterns = [
    path('product/<pk>', ProductRetrieveView.as_view()),
    path('product/', ProductListView.as_view()),
    path('product/search/', ProductSearchView.as_view()),
    path('product/manufacturer/<pk>', ProductManufacterFilter.as_view()),
    path('product/category/', ProductCategoryFilter.as_view()),
    path('product/producttype/', ProductTypeFilter.as_view()),
    path('manufacturer/name/', ManufacturerFilter.as_view()),
    path('category/name/', CategoryNameFilter.as_view()),
    path('product/producttype/name/', ProductTypeFilterNames.as_view()),
    path('product/Attribute/name/', ProductAttribuiteFilterNames.as_view()),
]
