from django.urls import include, path
from rest_framework import routers

from .views import GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('api/v1/posts', PostViewSet)
router.register('api/v1/posts', GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
