from rest_framework.routers import SimpleRouter
from .views import CatViewSet

router = SimpleRouter()
router.register('cats', CatViewSet)
