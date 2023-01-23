from django.urls import path
from rest_framework import routers

from . import views
from .views import PostAPIList, PostAPIDetail, PostAPIListByTag

app_name = 'blog'

#router = routers.DefaultRouter()
#router.register(r'blog', PostsViewSet, basename='posts')

urlpatterns = [
    path(r'posts/', views.PostAPIList.as_view(), name='posts'),
    path(r'posts/by-tag/<slug:slug>/', PostAPIListByTag.as_view(), name='posts-by-tag'),
    path(r'posts/<int:pk>', views.PostAPIDetail.as_view(), name='post-detail')
]
