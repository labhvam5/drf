from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def api_home(request):
    return JsonResponse({"message": "world is hello world"})