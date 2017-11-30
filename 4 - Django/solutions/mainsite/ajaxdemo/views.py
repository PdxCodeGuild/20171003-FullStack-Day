from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

def index(request):
    return render(request, 'ajaxdemo/index.html', {})

def getdata(request):
    data = {'name':'joe', 'age':2324}
    return JsonResponse(data)

def postdata(request):
    data = json.loads(request.body)
    print(data)
    return HttpResponse('OK')


