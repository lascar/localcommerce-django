import pdb
from django.test import TestCase
from products.views import index
from products.models import Product

class ProductIndexTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.product1 = Product.objects.create(name='product1', valid=True)
        self.product2 = Product.objects.create(name='product2', valid=True)
        self.product3 = Product.objects.create(name='product3', valid=False)

    def setUp(self):
        self.response = self.client.get('/products/')

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_return_list_available_products(self):
        products = self.response.context['products']
        # pdb.set_trace()
        self.assertTrue(self.product1 in products)
        self.assertTrue(self.product2 in products)
        self.assertFalse(self.product3 in products)
