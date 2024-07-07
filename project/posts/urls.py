from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet

router = SimpleRouter()

router.register('api/v1/posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]
