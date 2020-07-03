import pdb
from django.test import TestCase
from products.models import Product
from concrete_products.models import ConcreteProduct

class ConcretProductTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.product1 = Product.objects.create(name='product1', brands=['brand1', 'brand2'])
        self.concret_product1 = ConcreteProduct.objects.create(product_id=self.product1.id, brand='brand1')
        self.concret_product2 = ConcreteProduct.objects.create(product_id=self.product1.id, brand='brand2')

    def setUp(self):
        self.response = self.client.get('/concrete_products/')

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_return_list_of_concrete_products(self):
        concrete_products = self.response.context['concrete_products']
        # pdb.set_trace()
        self.assertTrue(self.concrete_product1 in products)
        self.assertTrue(self.concrete_product2 in products)
        self.assertEqual(concrete_products, 2)
