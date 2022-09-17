from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from core import views 
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your tests here.

class TestPost(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PostListCreate.as_view()
        self.uri = '/core/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        user = User
        return user.objects.create_user(
        'test',
        email='testuser@test.com',
        password='test'
        )

    def test_list(self):
        request = self.factory.get(self.uri,
        HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
        'Expected Response Code 200, received {0} instead.'
        .format(response.status_code))
