import pdb
from django.test import TestCase
from products.views import index
from products.models import Product

class ProductIndexTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.product1 = Product.objects.create(name='product1', active=True)
        self.product2 = Product.objects.create(name='product2', active=True)
        self.product3 = Product.objects.create(name='product3', active=False)

    def setUp(self):
        self.response = self.client.get('/products/')

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_return_list_available_products(self):
        # pdb.set_trace()
        products = self.response.context['products']
        b1 = next(filter(lambda obj: obj.get('name') == 'product1', products), None)
        b2 = next(filter(lambda obj: obj.get('name') == 'product2', products), None)
        b3 = next(filter(lambda obj: obj.get('name') == 'product3', products), None)
        self.assertTrue(isinstance(b1, (dict)))
        self.assertTrue(isinstance(b2, (dict)))
        self.assertFalse(isinstance(b3, (dict)))
