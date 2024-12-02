from django.contrib import admin
from django.urls import path, include  # Add include
# from .views import ModelViewSet      # Import your ModelViewSet
from .views import *                   # Import all views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('model-management', ModelViewSet, basename='model-management')

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    # path('index/', index, name='index'),
]

