from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model 

from .models import Post 

# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = "testuser",
            password="123456secret",
            email = "test@email.com",
        )

        self.post = Post.objects.create(
            title = "Test title",
            body= "Test body",
            author = self.user,
        )

   

    def test_str_representation(self):
        post = Post(title="Sample title")
        self.assertEqual(str(post), "Sample title")

    def test_post_content_in_db(self):
        current_post = Post.objects.get(id=1)
        self.assertEqual(current_post.title , "Test title")
        self.assertEqual(current_post.body,"Test body" )
        self.assertEqual(str(current_post.author), "testuser")

    def test_post_list_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_post_list_view_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test body")

    def test_detail_view_valid(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertContains(response, "Test body") 

    def test_detail_view_invalid(self):
        response = self.client.get('/post/10000000/')
        self.assertEqual(response.status_code, 404) 

    def test_absolute_url(self):
            self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title' : "New title", 
            "body" : "New body", 
            "author" : self.user,
            })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New title")
        self.assertContains(response, "New body")
        self.assertTemplateUsed(response, 'post_new.html')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title' : 'Updated title',
            'body' : 'Updated body',
        })
        self.assertEqual(response.status_code, 302)
        #self.assertTemplateUsed(response, 'post_edit.html')

    def test_post_delete_view(self):
        response = self.client.get(
            reverse('post_delete', args='1')
        )
        self.assertEqual(response.status_code, 200)

    

