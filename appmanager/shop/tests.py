from django.test import TestCase



class TestLogin(TestCase):
    def test_get(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, 200)

    def test_post(self):
        response = self.client.post('/login/')
        self.assertEquals(response.status_code, 302)

    def test_logout_func(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, 200)


class TestRegister(TestCase):
    def test_get(self):
        response = self.client.get('/register/')
        self.assertEquals(response.status_code, 200)


class TestShop(TestCase):
    def test_product_index(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_product_about(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)