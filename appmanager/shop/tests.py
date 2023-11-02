import unittest

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.test import TestCase
from django.urls import reverse
User = get_user_model()



class TestShop(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='shop/product/index.html')

    def test_about(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='shop/base.html')

    def test_login(self):
        response = self.client.get(reverse('shop:product_index'))
        self.assertEquals(response.status_code, 200)
    def test_post(self):
        username = 'test_username'

        payload = {
            'username': 'username',
            'password1': '1234@qwer',
        }
        response = self.client.post(reverse('shop:product_index'), data=payload)
        #user = User.object.get(username='test_username')
        #self.assertEquals(user.password, username)
        self.assertEquals(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(reverse('shop:product_index'))
        self.assertEquals(response.status_code, 200)

class TestRegisterView(TestCase):
    def test_get(self):
        response = self.client.get(reverse('shop:register'))
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.context['form'], UserCreationForm)



    def test_post(self):

        payload = {
            'username': 'username',
            'password1': '1234@qwer',
            'password2': '1234@qwer',
        }
        response = self.client.post(reverse('shop:register'), data=payload)
        self.assertEquals(response.status_code, 302)


    def test_post_errors(self):
        payload = {
            'username': 'username',
            'password1': '1234',
        }
        response = self.client.post(reverse('shop:register'), data=payload)
        self.assertEquals(response.status_code, 302)
        #self.assertIn('password1', response.context['form'].errors)


