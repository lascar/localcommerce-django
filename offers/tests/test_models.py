import pdb
from django.test import TestCase
from django.utils import timezone
from offers.models import Offer
from products.models import Product
from users.models import CustomUser
import django.db

class OfferModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user1 = CustomUser.objects.create(email='test@example.com',
                password='password')
        self.product1 = Product.objects.create(name='product1', valid=True,
                variety='variety1')
        self.offer1 = Offer.objects.create(user_id=self.user1.id,
                product_id=self.product1.id, unit_quantity=1,
                unit_price=2)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_valid(self):
        self.assertGreater(self.offer1.id, 0)

    def test_date_start(self):
        # pdb.set_trace()
        self.assertEqual(self.offer1.date_start.strftime("%m/%d/%Y"),
            timezone.now().strftime("%m/%d/%Y"))

    def test_create_invalid_without_user(self):
        with self.assertRaises(django.db.Error):
            Offer.objects.create(product_id=self.product1.id,
                    unit_quantity=1, unit_price=2)

    def test_create_invalid_without_product(self):
        # pdb.set_trace()
        with self.assertRaises(django.db.Error):
            Offer.objects.create(user_id=self.user1.id,
                    unit_quantity=1, unit_price=2)
