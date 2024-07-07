from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/posts/', views.api_posts),
    path('api/v1/posts/<int:pk>/', views.api_posts_detail)
]
