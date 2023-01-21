from django.test import TestCase

from blog.models import BlogPost
from blog.serializers import PostListSerializer, PostDetailSerializer


class PostListSerializerTestCase(TestCase):
    def test_ok(self):
        post1 = BlogPost.objects.create(title='post1', content='post1', image='images/2_Angry-Monkey.jpg')
        post2 = BlogPost.objects.create(title='post2', content='post2', image='images/2018_01_art_7_1_400.jpg')
        data = PostListSerializer([post2, post1], many=True).data
        expected_data = [
            {
                'id': post2.id,
                'title': 'post2',
                'content': 'post2',
                'tags': [],
                'thumbnail': '/CACHE/images/images/2018_01_art_7_1_400/139182dddf64f9b39118d00d46604f12.png'
            },
            {
                'id': post1.id,
                'title': 'post1',
                'content': 'post1',
                'tags': [],
                'thumbnail': '/CACHE/images/images/2_Angry-Monkey/6a4545ad490db60da4341cfddae874da.png'
            }
        ]

        self.assertEqual(expected_data, data)


class PostDetailSerializerTestCase(TestCase):
    def test_ok(self):
        post1 = BlogPost.objects.create(title='post1', content='post1', image='images/2_Angry-Monkey.jpg')
        data = PostDetailSerializer(post1).data
        expected_data = {
            'id': post1.id,
            'title': 'post1',
            'content': 'post1',
            'tags': [],
            'image': '/images/2_Angry-Monkey.jpg'
        }

        self.assertEqual(expected_data, data)
