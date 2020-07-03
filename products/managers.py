from django.db import models

class ProductManager(models.Manager):

    def valid(self):
        return self.filter(valid=True)
