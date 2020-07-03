# users/forms.py
import pdb
import datetime
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import ugettext as _
from .models import Offer

class OfferForm(forms.ModelForm):
    # pdb.set_trace()
    MONTHS = {
        1:_('jan'), 2:_('feb'), 3:_('mar'), 4:_('apr'),
        5:_('may'), 6:_('jun'), 7:_('jul'), 8:_('aug'),
        9:_('sep'), 10:_('oct'), 11:_('nov'), 12:_('dec')
    }
    date_start = forms.DateField(widget=AdminDateWidget, initial=datetime.date.today, required=True)
    date_end = forms.DateField(widget=forms.SelectDateWidget(months=MONTHS), initial=datetime.date.today, required=False)

    def clean_date_start(self):
        data = self.cleaned_data['date_start']
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - start in past'))
        return data

    def clean_date_end(self):
        data = self.cleaned_data_get['date_end']
        start = start 
        if data < start:
            raise ValidationError(_('Invalid date - end must be greater than start'))
        return data

    class Meta:
        model = Offer
        fields = ['concrete_product', 'user', 'unit_quantity', 'unit_price',
                'supplier_observation', 'date_start', 'date_end']
        labels = {
                'concrete_product': _('Concrete product'),
                'user': _('User'),
                'unit_quantity': _('Unit quantity'),
                'unit_price': _('Unit price'),
                'date_start': _('Date start'),
                'date_end': _('Date end'),
                }
