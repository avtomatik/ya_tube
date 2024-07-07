from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/posts/', views.api_posts, name='api_posts'),
]
