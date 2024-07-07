from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/posts/', views.APIPost.as_view()),
    path('api/v1/posts/<int:pk>/', views.APIPostDetail.as_view())
]
