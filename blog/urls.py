from django.urls import path
from rest_framework import routers

from . import views
from .views import PostAPIList, PostAPIDetail

app_name = 'blog'

#router = routers.DefaultRouter()
#router.register(r'blog', PostsViewSet, basename='posts')

urlpatterns = [
    path('posts', views.PostAPIList.as_view(), name='posts'),
    path('posts/<int:pk>', views.PostAPIDetail.as_view())
]
