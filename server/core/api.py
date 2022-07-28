from django.urls import path, include
from core.views.product_views import *

urlpatterns = [
    path('product/<pk>', ProductRetrieveView.as_view())
]
