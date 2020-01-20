from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='rae',
            email='ravend17@email.com',
            password='shiney1.'
        )

        self.post = Post.objects.create(
            title='Hawkeye',
            body='Series by Matt Fraction, superior to MCU Clint Barton',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='Hawkeye')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Hawkeye')
        self.assertEqual(f'{self.post.author}', 'rae')
        self.assertEqual(f'{self.post.body}', 'Series by Matt Fraction, superior to MCU Clint Barton')

    def test_post_list(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail(self):
        response = self.client.get('/detail/1/')
        no_response = self.client.get('/detail/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Hawkeye')
        self.assertTemplateUsed(response, 'detail.html')