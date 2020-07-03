from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from .managers import ProductManager
from django.utils.translation import ugettext_lazy as _
class Product(models.Model):
    valid = models.BooleanField(default=True)
    name = models.CharField(max_length=150, blank=False, default=None)
    brands = ArrayField(
                    models.CharField(max_length=20, blank=True, default=''),
                    default=list, blank=True
            )
    varieties = ArrayField(
                    models.CharField(max_length=20, blank=True, default=''),
                    default=list, blank=True
            )
    aspects = ArrayField(
                    models.CharField(max_length=20, blank=True, default=''),
                    default=list, blank=True
            )
    packagings = ArrayField(
                    models.CharField(max_length=20, blank=True, default=''),
                    default=list, blank=True
            )
    sizes = ArrayField(
                    models.CharField(max_length=20, blank=True, default=''),
                    default=list, blank=True
            )
    calibers = ArrayField(
                    models.CharField(max_length=20, blank=True, default=''),
                    default=list, blank=True
            )


    objects = ProductManager()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        constraints = [
            models.UniqueConstraint( fields=['name'], name='product_unique')
        ]

    def __str__(self):
        return self.name
