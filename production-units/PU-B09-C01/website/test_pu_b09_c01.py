from django.test import TestCase
from django.urls import reverse
class Book9Lesson1Tests(TestCase):
    def test_unit_page(self):
        response=self.client.get(reverse('catalog:unit_detail',kwargs={'code':'PU-B09-C01'}))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'AI Strategy and Transformation')
