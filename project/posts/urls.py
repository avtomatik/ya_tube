from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet, TagViewSet

router = routers.DefaultRouter()
router.register('api/v1/posts', PostViewSet)
router.register('api/v1/posts', TagViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
