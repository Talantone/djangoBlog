from rest_framework import serializers

from blog.models import BlogPost


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ("id", "title", "content", "tags", "thumbnail")

    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        return obj.thumbnail.url


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ("id", "title", "content", "tags", "image")

    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url
