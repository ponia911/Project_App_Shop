import unittest

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.test import TestCase
from django.urls import reverse



class TestShop(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, 200)

class TestRegisterView(TestCase):
    def test_get(self):
        response = self.client.get('/register/')
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.context['form'], UserCreationForm)

#class TestProductView(TestCase):
#    def test_product(self):
#        request = self.client.get('/football')
#        self.assertEquals(request.status_code, 200)