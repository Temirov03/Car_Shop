from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .serializers import AudiSerializer
from .views import AudiViewSet


router = DefaultRouter()

router.register('audi',AudiViewSet)

urlpatterns = [
    path('',include(router.urls))
]