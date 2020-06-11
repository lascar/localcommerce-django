from django.db import models
from django.conf import settings
from .managers import ProductManager
from django.utils.translation import ugettext_lazy as _
class Product(models.Model):
    valid = models.BooleanField(default=True)
    name = models.CharField(max_length=150)
    variety = models.CharField(max_length=150)

    objects = models.Manager()
    browser = ProductManager()

    class Meta:
        verbose_name_plural = _('Products')
        constraints = [
            models.UniqueConstraint(fields=['name', 'variety'], name='product_unique')
        ]

    def __str__(self):
        return self.name + ' : ' + self.variety
