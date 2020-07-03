import pdb
import datetime
from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.core.validators import MinValueValidator
from .managers import OfferManager
from concrete_products.models import ConcreteProduct
from users.models import CustomUser
from django.utils.translation import ugettext_lazy as _

class Offer(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    concrete_product =  models.ForeignKey(to=ConcreteProduct, on_delete=models.CASCADE)
    unit_quantity = models.PositiveIntegerField(_('quantity'),
            validators=[MinValueValidator(1)], default=1)
    unit_price = models.DecimalField(decimal_places=4, max_digits=22, default=0.01, \
            validators=[MinValueValidator(0)])
    supplier_observation = models.TextField("supplier's observation", \
            max_length=150, blank=True)
    date_start = models.DateField(default=datetime.date.today, blank=True, \
            validators=[MinValueValidator(datetime.date.today)])
    date_end = models.DateField( \
            default=(datetime.date.today), \
                blank=True, validators=[MinValueValidator(datetime.date.today)])
    valid = models.BooleanField(default=True)
    # pdb.set_trace()

    objects = OfferManager()

    def get_absolute_url(self):
        return reverse('offer_detail', args=[str(self.id)])

    def product_name(self):
        return self.concrete_product.name + ':' + self.concrete_product.variety

    @property
    def user_email(self):
        return self.user.email

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')

    def __str__(self):
        return (self.product_name() + ' : ' \
                + self.date_start.strftime("%d/%m/%Y") + ' : ' \
                + self.date_end.strftime("%d/%m/%Y"))
