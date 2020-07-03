import pdb
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ConcreteProduct
from .forms import ConcreteProductForm
from django.utils.translation import ugettext_lazy as _

def index(request):
    # TODO: filter by my concrete_products as user
    # pdb.set_trace()
    form = ConcreteProductForm()
    context = {'concrete_products': ConcreteProduct.objects.all(), 'form': form}
    return render(request, 'concrete_products_index.html', context)

def detail(request, id):
    context = {}
    context['concrete_product'] = ConcreteProduct.objects.get(id=id)
    return render(request, 'concrete_product_detail.html', context)

def create(request):
    form = ConcreteProductForm(request.POST)
    if form.is_valid(): 
        try:
            form.save()
            return redirect('detail')
        except:
            pass
