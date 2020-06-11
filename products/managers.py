from django.db import models

class ProductManager(models.Manager):
    def non_valid(self):
        return self.filter(valid=False)

    def valid(self):
        return self.filter(valid=True)
