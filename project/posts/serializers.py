from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    character_quantity = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id', 'text', 'author', 'image', 'pub_date', 'character_quantity'
        )
        model = Post

    def get_character_quantity(self, obj):
        return len(obj.text)
