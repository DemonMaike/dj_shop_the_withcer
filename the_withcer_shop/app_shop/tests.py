from django.test import TestCase


class Code200TestCase(TestCase):
    """Class for testing of pages on status code 200"""

    def test_home_200(self):
        """Testing the homepage"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
            
    def test_about_200(self):
        """Testing the about page"""
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_category_200(self):
        """Testing the category page"""
        response = self.client.get('/category')
        self.assertEqual(response.status_code, 200)

    def test_allproducts_200(self):
        """Testing the allproducts page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)