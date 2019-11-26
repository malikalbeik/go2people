from django.shortcuts import loader
from django.http import HttpResponse

from .models import Product


def index(request):
    products = Product.objects.all()
    template = loader.get_template("shop/index.html")
    context = {
        "products": products,
    }
    return HttpResponse(template.render(context, request))
