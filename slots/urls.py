from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SlotViewSet

router = DefaultRouter()
router.register(r'', SlotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
