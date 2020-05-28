import pdb
from django.shortcuts import render
from .models import Product

def index(request):
    # pdb.set_trace()
    context = {'products': __make_products(Product.browser.active())}
    return render(request, 'index.html', context)

def __make_products(products):
    list_products = list(map(__make_product, products))
    return list_products

def __make_product(product):
    varieties_string = ', '.join(product.varieties)
    aspects_string = ', '.join(product.aspects)
    packagings_string = ', '.join(product.packagings)
    sizes_string = ', '.join(product.sizes)
    calibers_string = ', '.join(product.calibers)
    return {'name': product.name, 'varieties': varieties_string,
            'aspects': aspects_string, 'packagings': packagings_string,
            'sizes': sizes_string, 'calibers': calibers_string}

