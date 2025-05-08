from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParcelViewSet

router = DefaultRouter()
router.register(r'', ParcelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
