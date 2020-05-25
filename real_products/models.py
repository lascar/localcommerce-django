import pdb
from django.db.models.signals import pre_save
from django.db import models
from .managers import RealProductManager
from products.models import Product
from django.utils.translation import ugettext_lazy as _
class RealProduct(models.Model):
    name = models.CharField(max_length=150, blank=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    variety = models.CharField(max_length=150, blank=True)
    aspect = models.CharField(max_length=150, blank=True)
    packaging = models.CharField(max_length=150, blank=True)
    size = models.CharField(max_length=150, blank=True)
    caliber = models.CharField(max_length=150, blank=True)


    objects = models.Manager()
    browser = RealProductManager()

    class Meta:
        verbose_name = _('Real Product')
        verbose_name_plural = _('Real Products')

    def __str__(self):
        return self.name

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        # pdb.set_trace()
        instance.name = instance.product.name
        instance.variety = (_('not precised'), instance.variety)[instance.variety in instance.product.varieties]
        instance.aspect = (_('not precised'), instance.aspect)[instance.aspect in instance.product.aspects]
        instance.packaging = (_('not precised'), instance.packaging)[instance.packaging in instance.product.packagings]
        instance.size = (_('not precised'), instance.size)[instance.size in instance.product.sizes]
        instance.caliber = (_('not precised'), instance.caliber)[instance.caliber in instance.product.calibers]

pre_save.connect(RealProduct.pre_save, RealProduct, dispatch_uid='real_products.models.CustomUser')
