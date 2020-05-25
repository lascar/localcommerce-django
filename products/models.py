from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.conf import settings
from .managers import ProductManager
from django.utils.translation import ugettext_lazy as _
class Product(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=150)
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


    objects = models.Manager()
    browser = ProductManager()
    # product_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = _('Products')
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_by_name'),
        ]

    def __str__(self):
        return self.name
