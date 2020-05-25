from django.db import models

class ProductManager(models.Manager):
    def non_active(self):
        return self.filter(active=False)

    def active(self):
        return self.filter(active=True)
