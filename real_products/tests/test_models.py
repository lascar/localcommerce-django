import pdb
from django.test import TestCase
from real_products.models import RealProduct
from products.models import Product
from django.utils.translation import ugettext_lazy as _
import django.db

class RealProductModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Run once to set up non-modified data for all class methods.
        self.product1 = Product.objects.create(name='product1', active=True,
                         varieties=['variety1', 'variety2'],
                         aspects=['aspect1', 'aspect2'],
                         packagings=['packaging1', 'packaging2'],
                         sizes=['size1', 'size2'],
                         calibers=['caliber1', 'caliber2'])
        self.real_product1 = RealProduct.objects.create(product_id=self.product1.id,
                aspect='aspect1', packaging='packaging')


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_name_equal_product_name(self):
        self.assertEquals(self.real_product1.name, self.product1.name)

    def test_variety_equal_product_name(self):
        self.assertEquals(self.real_product1.variety, _('not precised'))

    def test_aspect_equal_one_of_product_aspects(self):
        self.assertEquals(self.real_product1.aspect, 'aspect1')

    def test_packaging_equal_not_precised(self):
        self.assertEquals(self.real_product1.packaging, _('not precised'))

    def test_size_equal_not_precised(self):
        self.assertEquals(self.real_product1.size, _('not precised'))

    def test_caliber_equal_not_precised(self):
        self.assertEquals(self.real_product1.caliber, _('not precised'))

