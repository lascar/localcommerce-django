# users/forms.py
import pdb
from django import forms
from django.utils.translation import ugettext as _
from .models import ConcreteProduct

class ConcreteProductForm(forms.ModelForm):
    # pdb.set_trace()

    class Meta:
        model = ConcreteProduct
        fields = ['name', 'product', 'brand', 'variety', 'aspect',
            'packaging', 'size', 'caliber']
        labels = {
                'name': _('Name'),
                'product': _('Product'),
                'brand': _('Brand'),
                'variety': _('Variety'),
                'aspect': _('Aspect'),
                'packaging': _('Packaging'),
                'size': _('Size'),
                'caliber': _('Caliber'),
                }
