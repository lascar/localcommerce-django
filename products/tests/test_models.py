import pdb
from django.test import TestCase
from products.models import Product
import django.db

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Run once to set up non-modified data for all class methods.
        self.product1 = Product.objects.create(name='product1', active=True,\
                         varieties=['variety1', 'variety2'],\
                         aspects=['aspect1', 'aspect2'],\
                         packagings=['packaging1', 'packaging2'],\
                         sizes=['size1', 'size2'],\
                         calibers=['caliber1', 'caliber2'])

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_product_create(self):
        self.assertEquals(self.product1.name, 'product1')
        self.assertTrue(self.product1.active)
        self.assertEquals(self.product1.varieties, ['variety1', 'variety2'])
        self.assertEquals(self.product1.aspects, ['aspect1', 'aspect2'])
        self.assertEquals(self.product1.packagings, ['packaging1', 'packaging2'])
        self.assertEquals(self.product1.sizes, ['size1', 'size2'])
        self.assertEquals(self.product1.calibers, ['caliber1', 'caliber2'])

    def test_unique_name(self):
        # pdb.set_trace()
        with self.assertRaises(django.db.Error):
            Product.objects.create(name='product1')
