from django.db import models

class ProductManager(models.Manager):
    def non_active(self):
        return self.filter(active=False)

    def active(self):
        return self.filter(active=True)

    def category(self, category):
        return self.filter(category=category)
