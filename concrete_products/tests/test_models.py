import pdb
from django.test import TestCase
from concrete_products.models import ConcreteProduct
from products.models import Product
from django.utils.translation import ugettext_lazy as _
import django.db

class ConcreteProductModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Run once to set up non-modified data for all class methods.
        self.product1 = Product.objects.create(name='product1', valid=True,
                         brands=['brand1', 'brand2'],
                         varieties=['variety1', 'variety2'],
                         aspects=['aspect1', 'aspect2'],
                         packagings=['packaging1', 'packaging2'],
                         sizes=['size1', 'size2'],
                         calibers=['caliber1', 'caliber2'])
        self.product2 = Product.objects.create(name='product2', valid=False)
        self.concrete_product1 = ConcreteProduct.objects.create(product_id=self.product1.id,
                aspect='aspect1', packaging='packaging')


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_name_equal_product_name(self):
        self.assertEquals(self.concrete_product1.name, self.product1.name)

    def test_variety_equal_product_name(self):
        self.assertEquals(self.concrete_product1.variety, _('not precised'))

    def test_aspect_equal_one_of_product_aspects(self):
        self.assertEquals(self.concrete_product1.aspect, 'aspect1')

    def test_packaging_equal_not_precised(self):
        self.assertEquals(self.concrete_product1.packaging, _('not precised'))

    def test_size_equal_not_precised(self):
        self.assertEquals(self.concrete_product1.size, _('not precised'))

    def test_caliber_equal_not_precised(self):
        self.assertEquals(self.concrete_product1.caliber, _('not precised'))

    def test_create_product_invalide_raise_error(self):
        with self.assertRaises(django.db.Error):
            ConcreteProduct.objects.create(product_id=self.product2.id)
