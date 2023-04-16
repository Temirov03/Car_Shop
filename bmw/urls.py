from rest_framework.routers import SimpleRouter
from django.urls import path,include
from .views import BMWViewSet,CaptivaViewSet


router = SimpleRouter()

router.register('bmw', BMWViewSet)
router.register('captiva',CaptivaViewSet)


urlpatterns = [
]
