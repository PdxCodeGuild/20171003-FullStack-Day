from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TodoAjaxItem
import json

# Create your views here.

def index(request):
    return render(request, 'todoajax/index.html')


def savetodo(request):
    data = json.loads(request.body)
    todo_text = data['todo_text']
    todo_item = TodoAjaxItem(text=todo_text)
    todo_item.save()
    return HttpResponse('ok')


def gettodos(request):
    output = {'todo_items': []}
    todo_items = TodoAjaxItem.objects.all()
    for todo_item in todo_items:
        output['todo_items'].append(todo_item.text)
    return JsonResponse(output)



