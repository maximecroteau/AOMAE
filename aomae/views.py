from django.shortcuts import render
from .models import Products
# Create your views here.


def index(request):
    Prds = Products.objects.all()
    BestRates = Products.objects.filter(stars__gte=4)
    return render(request, 'index.html', {
        'Prds': Prds,
        'BestRates': BestRates,
    })


def shop(request):

    return render(request, 'shop.html')


def contact(request):

    return render(request, 'contact.html')


def cart(request):

    return render(request, 'cart.html')


def checkout(request):

    return render(request, 'checkout.html')


def thankyou(request):

    return render(request, 'thankyou.html')


