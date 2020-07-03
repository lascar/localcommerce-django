import pdb
from django.test import TestCase
from offers.views import index
from products.models import Product
from users.models import CustomUser
from offers.models import Offer

class OfferIndexTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user1 = CustomUser.objects.create(email='test@example.com',
                password='password')
        self.product1 = Product.objects.create(name='product1', valid=True,
                variety='variety1')
        self.product2 = Product.objects.create(name='product2', valid=True,
                variety='variety3')
        self.product3 = Product.objects.create(name='product3', valid=True,
                variety='variety5')
        self.offer1 = Offer.objects.create(user_id=self.user1.id,
                product_id=self.product1.id, unit_quantity=1,
                unit_price=2)
        self.offer2 = Offer.objects.create(user_id=self.user1.id,
                product_id=self.product2.id, unit_quantity=2,
                unit_price=4)
        self.offer3 = Offer.objects.create(user_id=self.user1.id,
                product_id=self.product3.id, unit_quantity=3,
                unit_price=6)
        self.user1.products = [self.product1, self.product2]

    def setUp(self):
        self.response = self.client.get('/offers/')

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_return_list_offers_for_anonymous(self):
        offers = self.response.context['offers']
        self.assertEqual(offers[0].unit_quantity, 1)
        self.assertEqual(offers[1].unit_quantity, 2)
        self.assertEqual(offers[2].unit_quantity, 3)
        self.assertEqual(offers.count(), 3)
        # pdb.set_trace()

    # def test_return_list_offers_with_only_product_of_interest(self):
    #     offers = self.response.context['offers']
    #     self.assertEqual(offers[0].unit_quantity, 1)
    #     self.assertEqual(offers[1].unit_quantity, 2)
    #     self.assertEqual(offers.count(), 2)
    #     # pdb.set_trace()
