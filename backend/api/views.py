from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def api_home(request, *args, **kwargs):
    body = request.body
    # print(body)
    try:
        data = json.loads(body)
        # print(data)
        params = request.GET
        print(params)
    except Exception as error:
        return JsonResponse({"error": error})
    # return JsonResponse({"msg": "Hi there! This is your Django API response !"})
    # return JsonResponse({"msg": "Hi there! This is your Django API response !"})
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    data["params"] = dict(request.GET)
    return JsonResponse(data)