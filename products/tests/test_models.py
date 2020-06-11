import pdb
from django.test import TestCase
from products.models import Product
import django.db

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Run once to set up non-modified data for all class methods.
        self.product1 = Product.objects.create(name='product1', valid=True,
                         variety='variety1')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_product_create(self):
        self.assertEquals(self.product1.name, 'product1')
        self.assertTrue(self.product1.valid)
        self.assertEquals(self.product1.variety, 'variety1')

    def test_unique_name(self):
        # pdb.set_trace()
        with self.assertRaises(django.db.Error):
            Product.objects.create(name='product1', variety='variety1')
