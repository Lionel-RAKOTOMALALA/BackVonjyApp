from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommuneViewSet

# Router DRF
router = DefaultRouter()
router.register(r'communes', CommuneViewSet, basename='commune')

urlpatterns = [
    path('', include(router.urls)),
]
