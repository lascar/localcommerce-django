import pdb
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Offer 
from .forms import OfferForm
from products.models import Product
from django.utils.translation import ugettext_lazy as _

def index(request):
    # TODO: filter by my offers as user
    # pdb.set_trace()
    form = OfferForm()
    context = {'offers': Offer.objects.all(), 'form': form}
    return render(request, 'offers_index.html', context)

def detail(request, id):
    context = {}
    context['offer'] = Offer.objects.get(id=id)
    return render(request, 'offer_detail.html', context)

def create(request):
    form = OfferForm(request.POST)
    if form.is_valid(): 
        try:
            form.save()
            return redirect('detail')
        except:
            pass
