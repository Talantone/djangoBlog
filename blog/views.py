from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404

from .models import BlogPost
from .serializers import PostDetailSerializer, PostListSerializer


class PostAPIList(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = BlogPost.objects.all().order_by('-id')

    def get_queryset(self):
        queryset = self.queryset.all()
        if len(queryset) > 2:
            return queryset[0:3]
        else:
            return queryset


class PostAPIDetail(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = BlogPost.objects.all()


