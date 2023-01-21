from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from blog import views
from blog.models import BlogPost
from blog.serializers import PostListSerializer, PostDetailSerializer


class PostsAPITestCase(APITestCase):


    #tests if API returns 3 last posts in response
    def test_get_posts_list(self):
        post1 = BlogPost.objects.create(title='post1', content='post1', image='images/2_Angry-Monkey.jpg')
        post2 = BlogPost.objects.create(title='post2', content='post2', image='images/2018_01_art_7_1_400.jpg')
        post3 = BlogPost.objects.create(title='post3', content='post3',
                                        image='images/monkey-day-heres-when-it-is-celebrated.jpg')
        post4 = BlogPost.objects.create(title='post4', content='post4', image='images/priroda_obezyyany_vzglyad.jpg')
        url = reverse('blog:posts')
        response = self.client.get(url)
        serializer_data = PostListSerializer([post4, post3, post2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    #tests if API returns valid details for one post
    def test_get_post_detail(self):
        post1 = BlogPost.objects.create(title='post1', content='post1', image='images/2_Angry-Monkey.jpg')
        url = reverse('blog:post-detail', args=[post1.pk])
        response = self.client.get(url)
        serializer_data = PostDetailSerializer(post1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
