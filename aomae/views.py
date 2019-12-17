from django.shortcuts import render, redirect

from .models import Products
from .models import Color

from .forms import AddToCartForm


def get_data():
    homme = Products.objects.filter(gender__contains="Homme").count()
    femme = Products.objects.filter(gender__contains="Femme").count()
    unisex = Products.objects.filter(gender__contains="Unisex").count()
    all_products = Products.objects.all()
    best_rates = Products.objects.filter(stars__gte=4)
    return homme, femme, unisex, all_products, best_rates


def index(request):
    homme, femme, unisex, all_products, best_rates = get_data()

    return render(request, 'index.html', {
        'Prds': all_products,
        'BestRates': best_rates,
        'nbHomme': homme,
        'nbFemme': femme,
        'nbUnisex': unisex,
    })


def shop(request):
    homme, femme, unisex, all_products, best_rates = get_data()

    return render(request, 'shop.html', {
        'Prds': all_products,
    })


def shop_filter(request, filt):
    if filt == "homme" or filt == "femme" or filt == "unisex":
        prds = Products.objects.filter(gender__contains=filt)
    elif filt == "alpha":
        prds = Products.objects.order_by('name')
    elif filt == "croissant":
        prds = Products.objects.order_by('price')
    elif filt == "decroissant":
        prds = Products.objects.order_by('-price')
    else:
        prds = Products.objects.all()

    return render(request, 'shop.html', {
        'Prds': prds,
    })


def product(request, pk):
    form = AddToCartForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        fpk = data['product_id']
        color = data['product_color']
        size = data['product_size']
        if 'cart' not in request.session or not request.session['cart']:
            cart_list = [fpk, color, size]
            request.session['cart'] = cart_list
            request.session.modified = True
        else:
            cart_list = request.session['cart']
            cart_list.append([fpk, color, size])
            request.session['cart'] = cart_list
            request.session.modified = True
        return redirect('cart')
    this = Products.objects.get(pk=pk)
    colors = Color.objects.filter(products__pk=pk)
    return render(request, 'product.html', {
        'product': this,
        'colors': colors,
    })


def contact(request):

    return render(request, 'contact.html')


def cart(request):
    all_cart = []
    if request.session.get('cart'):
        cs = request.session.get('cart')
        dic = {
            "product": Products.objects.get(pk=cs[0]),
            "color": cs[1],
            "size": cs[2]
        }
        all_cart.append(dic)
        if len(cs) > 3:
            for i in range(3, len(cs)):
                dic = {
                    "product": Products.objects.get(pk=cs[i][0]),
                    "color": cs[i][1],
                    "size": cs[i][2]
                }
                all_cart.append(dic)

    return render(request, 'cart.html', {
        'carts': all_cart,
    })


def checkout(request):

    return render(request, 'checkout.html')


def thankyou(request):

    return render(request, 'thankyou.html')


