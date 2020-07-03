import pdb
from django.db.models.signals import pre_save
from django.db import models
from .managers import ConcreteProductManager
from products.models import Product
from django.utils.translation import ugettext_lazy as _
class ConcreteProduct(models.Model):
    name = models.CharField(max_length=150, blank=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=150, blank=True)
    variety = models.CharField(max_length=150, blank=True)
    aspect = models.CharField(max_length=150, blank=True)
    packaging = models.CharField(max_length=150, blank=True)
    size = models.CharField(max_length=150, blank=True)
    caliber = models.CharField(max_length=150, blank=True)


    objects = ConcreteProductManager()

    class Meta:
        verbose_name = _('Concrete Product')
        verbose_name_plural = _('Concrete Products')
        constraints = [
            models.UniqueConstraint( fields=['name', 'brand', 'variety', 'aspect', 'packaging', 'size', 'caliber'], name='concrete_product_unique'),
        ]

    def __str__(self):
        return self.name + ':' + self.variety + ':' + self.aspect + ':' + self.packaging + ':' + self.size + ':' + self.caliber

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        # pdb.set_trace()
        instance.name = instance.product.name
        instance.brand = (_('not precised'), instance.brand)[instance.brand in instance.product.brands]
        instance.variety = (_('not precised'), instance.variety)[instance.variety in instance.product.varieties]
        instance.aspect = (_('not precised'), instance.aspect)[instance.aspect in instance.product.aspects]
        instance.packaging = (_('not precised'), instance.packaging)[instance.packaging in instance.product.packagings]
        instance.size = (_('not precised'), instance.size)[instance.size in instance.product.sizes]
        instance.caliber = (_('not precised'), instance.caliber)[instance.caliber in instance.product.calibers]
        instance.product = ( None, instance.product )[instance.product.valid]

pre_save.connect(ConcreteProduct.pre_save, ConcreteProduct, dispatch_uid='concrete_products.models.CustomUser')
