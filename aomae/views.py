from django.shortcuts import render, redirect
from django.forms import model_to_dict

from .models import Products
from .models import Color

from .forms import AddToCartForm
from .forms import RemFromCartForm
from .forms import ContactForm


def get_data():
    homme = Products.objects.filter(gender__contains="Homme").count()
    femme = Products.objects.filter(gender__contains="Femme").count()
    unisex = Products.objects.filter(gender__contains="Unisex").count()
    all_products = Products.objects.all()
    best_rates = Products.objects.filter(stars__gte=4)
    return homme, femme, unisex, all_products, best_rates


def get_nbcart(request):
    nbr = request.session.get('cart')
    i = 0
    if nbr:
        for nb in nbr:
            i = i + 1
            nbr = i
        return nbr
    else:
        return ""


def index(request):
    nb = get_nbcart(request)
    homme, femme, unisex, all_products, best_rates = get_data()
    return render(request, 'index.html', {
        'Prds': all_products,
        'BestRates': best_rates,
        'nbHomme': homme,
        'nbFemme': femme,
        'nbUnisex': unisex,
        'nb': nb,
    })


def shop(request):
    nb = get_nbcart(request)
    homme, femme, unisex, all_products, best_rates = get_data()

    return render(request, 'shop.html', {
        'Prds': all_products,
        'nb': nb,
    })


def shop_filter(request, filt):
    nb = get_nbcart(request)
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
        'nb': nb,
    })


def product(request, pk):
    nb = get_nbcart(request)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        fpk = data['product_id']
        color = data['product_color']
        size = data['product_size']
        url = Products.objects.get(pk=fpk).picture.url
        if 'cart' not in request.session or not request.session['cart']:
            pk = 0
            cart_list = [(pk, model_to_dict(Products.objects.get(pk=fpk), fields=['name', 'price']), url, color, size)]
            request.session['cart'] = cart_list
            request.session.modified = True
        else:
            cart_list = request.session['cart']
            pk = cart_list[-1][0] + 1
            cart_list.append((pk, model_to_dict(Products.objects.get(pk=fpk), fields=['name', 'price']), url, color, size))
            request.session['cart'] = cart_list
            request.session.modified = True

        return redirect('cart')
    this = Products.objects.get(pk=pk)
    colors = Color.objects.filter(products__pk=pk)
    return render(request, 'product.html', {
        'product': this,
        'colors': colors,
        'nb': nb,
    })


def contact(request):
    nb = get_nbcart(request)
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'contact.html', {
        'nb': nb,
    })


def cart(request):
    nb = get_nbcart(request)
    if request.session.get('cart'):
        cs = request.session.get('cart')
    else:
        cs = []
    form = RemFromCartForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        val = data['toRem'].split(";")
        lst = {'name': val[1], 'price': int(val[2])}
        dic = [int(val[0]), lst, val[3], val[4], val[5]]
        cs.remove(dic)
        request.session.modified = True

        return redirect('cart')

    return render(request, 'cart.html', {
        'carts': cs,
        'nb': nb,
    })


def checkout(request):
    nb = get_nbcart(request)
    if request.session.get('cart'):
        cs = request.session.get('cart')
    else:
        cs = []

    return render(request, 'checkout.html', {
        'carts': cs,
        'nb': nb,
    })


def about(request):
    nb = get_nbcart(request)

    return render(request, 'about.html', {
        'nb': nb,
    })


def thankyou(request):
    nb = get_nbcart(request)

    return render(request, 'thankyou.html', {
        'nb': nb,
    })


