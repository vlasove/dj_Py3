from django.test import TestCase
from django.urls import reverse

from .models import Post 

# Create your tests here.
class PostModelTests(TestCase):
    # Определить метод для наполнения промежуточной БД
    def setUp(self):
        """
        Этот метод будет выполнен самым первым
        """
        Post.objects.create(text="this is test text")

    def test_text_content(self):
        current_post = Post.objects.get(id=1)
        expected_text = current_post.text

        self.assertEqual(expected_text, "this is test text")

    def tierDown(self):
        """
        После всех тестов
        """
        pass


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is test text')

    def test_view_url_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
