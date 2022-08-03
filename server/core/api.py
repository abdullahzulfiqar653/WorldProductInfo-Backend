from django.urls import path
from core.views import *


urlpatterns = [
    path('category/', CategoryListView.as_view()),
]
