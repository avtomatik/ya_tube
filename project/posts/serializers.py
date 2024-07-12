from rest_framework import serializers

from .models import Group, Post, Tag, TagPost


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Group.objects.all(),
        required=False
    )
    tag = TagSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group', 'tag')

    def create(self, validated_data):
        if 'tag' not in self.initial_data:
            post = Post.objects.create(**validated_data)
            return post

        tag = validated_data.pop('tag')
        post = Post.objects.create(**validated_data)
        for tag_particular in tag:
            current_tag, status = Tag.objects.get_or_create(**tag_particular)
            TagPost.objects.create(tag=current_tag, post=post)
        return post
