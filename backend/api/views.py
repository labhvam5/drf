from django.shortcuts import render
from django.http import JsonResponse
from products.models import Products
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
# Create your views here.

@api_view(["GET"])
def api_home(request):
    prod = Products.objects.all()[0]
    if prod:
        res = model_to_dict(prod)
    else:
        res = {"error": "Product not found"}
        Response(res, status=500)

    return Response(res, status=HTTP_500_INTERNAL_SERVER_ERROR)