from rest_framework.routers import DefaultRouter
from .views import DreamViewSet

router = DefaultRouter()
router.register(r'dreams', DreamViewSet, basename='dream')

urlpatterns = router.urls