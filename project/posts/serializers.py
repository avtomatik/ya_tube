from rest_framework import serializers

from .models import Group, Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug')


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        required=False,
        queryset=Group.objects.all(),
        slug_field='slug'
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group')
