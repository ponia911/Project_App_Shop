
from django.test import TestCase
from cart.cart import Cart
from cart.views import cart_remove, cart_about



class TestCart(TestCase):

    def test_cart_add(self):
        response = self.client.post('/cart/')
        self.assertEquals(response.status_code, 200)

    def test_cart_remove(self):
        request = self.client.post('/cart:cart_about/', {})
        self.session = request.session
        Cart(request).add(product=self.product, quantity=1)
        response = cart_remove(request, product_id=self.product.id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart:cart_about/')

    def test_cart_about(self):
        request = self.client.get('/cart:cart_about/')
        self.session = request.session
        Cart(request).add(product=self.product, quantity=1)
        response = cart_about(request)
        self.assertEqual(response.status_code, 200)


