from rest_framework.routers import DefaultRouter
from library.models import Book
from library.views import BookOperations
router = DefaultRouter()
router.register('api',BookOperations)

urlpatterns = router.urls