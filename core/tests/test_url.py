from http import client
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from core.views import ApiGenerics
from rest_framework.test import APITestCase,APIClient
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token 

from core.views import ApiGenerics

class ApiUrlsTests(SimpleTestCase):

    def test_create_resolved(self):
        url = reverse('create')
        #print(resolve(url).func)
        self.assertEqual(resolve(url).func.view_class,ApiGenerics)

class PostAPITest(APITestCase):
    posts_urls = reverse('create')

    def setUp(self):
        self.user = User.objects.create(username='admin',password='admin',email='admin@admin.com')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def tearDown(self):
        pass 

    def test_get_post(self):
        response = self.client.get(self.posts_urls)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_post_false(self):
        self.client.force_authenticate(user=None,token=None)
        response = self.client.get(self.posts_urls)
        self.assertEqual(response.status_code,401)

    def test_post_true(self):
        data = {
            "title":"MR",
            "content":"post",
            "owner":1,
            'slug':""
        }
        response = self.client.post(self.posts_urls,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], 'post')