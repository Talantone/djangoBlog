from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404

from .models import BlogPost, Tag
from .serializers import PostDetailSerializer, PostListSerializer


class PostAPIList(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = BlogPost.objects.all().order_by('-id')

    #function for returning 3 last posts
    def get_queryset(self):
        queryset = self.queryset.all()
        if len(queryset) > 2:
            return queryset[0:3]
        else:
            return queryset


class PostAPIDetail(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = BlogPost.objects.all()


class PostAPIListByTag(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = BlogPost.objects.all()

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        tag = Tag.objects.get(slug=slug)
        queryset = self.queryset.filter(tags=tag)
        return queryset
