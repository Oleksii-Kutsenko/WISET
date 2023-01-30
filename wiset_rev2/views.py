import datetime
import json
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from wiset_rev2.models import Product
from .forms import MoneyForm, ProductForm


def gen_to_buy(to_buy_products, query, money):
    query = query.filter(
        price__lte=money,
        price__gt=0,
        in_fridge=False,
        season_start__lte=datetime.date.today(),
        season_end__gte=datetime.date.today(),
    ).exclude(name__in=[product.name for product in to_buy_products])
    if query.count() == 0:
        return to_buy_products
    product = query[random.randint(0, query.count() - 1)]
    to_buy_products.append(product)
    return gen_to_buy(to_buy_products, query, money - product.price)


@csrf_exempt
def add_to_fridge(request):
    data = json.loads(request.body)["data"]
    for id in data.keys():
        model = Product.objects.get(id=int(id))
        model.name = data[id]["name"]
        model.price = data[id]["price"]
        model.category = data[id]["category"]
        model.in_fridge = data[id]["in_fridge"]
        model.save()
    return HttpResponse(status=200)


def index(request):
    if request.method == "POST":
        form = MoneyForm(request.POST)
        if form.is_valid():
            to_buy = gen_to_buy([], Product.objects, form.cleaned_data["money_amount"])
            zero_price_products = Product.objects.filter(price=0).all()
            if zero_price_products.count() > 0:
                to_buy.append(
                    zero_price_products[
                        random.randint(0, zero_price_products.count() - 1)
                    ]
                )
            to_buy_forms = [
                ProductForm(
                    initial={
                        "id": product.id,
                        "name": product.name,
                        "price": product.price,
                        "category": product.category,
                        "in_fridge": product.in_fridge,
                    }
                )
                for product in to_buy
            ]
            return render(request, "add_to_fridge.html", {"to_buy": to_buy_forms})
    else:
        form = MoneyForm()
    return render(request, "index.html", {"form": form})
