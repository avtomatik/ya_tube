from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer


def get_post(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return JsonResponse(data=serializer.data)
