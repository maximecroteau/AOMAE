from django.shortcuts import render
from .models import Products
# Create your views here.


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
    this = Products.objects.get(pk=pk)
    return render(request, 'product.html', {
        'product': this,
    })


def contact(request):

    return render(request, 'contact.html')


def cart(request):

    return render(request, 'cart.html')


def checkout(request):

    return render(request, 'checkout.html')


def thankyou(request):

    return render(request, 'thankyou.html')


