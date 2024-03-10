from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product

# Create your views here.
# def api_home(request, *args, **kwargs):
#     body = request.body
#     # print(body)
#     try:
#         data = json.loads(body)
#         # print(data)
#         params = request.GET
#         print(params)
#     except Exception as error:
#         return JsonResponse({"error": error})
#     # return JsonResponse({"msg": "Hi there! This is your Django API response !"})
#     # return JsonResponse({"msg": "Hi there! This is your Django API response !"})
#     data["headers"] = dict(request.headers)
#     data["content_type"] = request.content_type
#     data["params"] = dict(request.GET)
#     return JsonResponse(data)

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data = model_data
        data["id"]=model_data.id
        data["title"]=model_data.title
        data["content"]=model_data.content
        data["price"]=model_data.price
    return JsonResponse(data)