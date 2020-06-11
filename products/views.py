import pdb
from django.shortcuts import render
from .models import Product

def index(request):
    # pdb.set_trace()
    context = {'products': Product.browser.valid()}
    return render(request, 'index.html', context)
