from django.test import Client, TestCase


class UrlsTestCase(TestCase):

    def test_home_url(self):
        response = Client().get('/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_admin_url(self):
        response = Client().get('/admin/', follow=True)
        self.assertEqual(response.status_code, 200)
