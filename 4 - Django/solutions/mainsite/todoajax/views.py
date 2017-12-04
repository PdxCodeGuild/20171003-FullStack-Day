from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import TodoItem

def index(request):
    return render(request, 'todoajax/index.html', {})



def gettodos(request):
    todo_items = TodoItem.objects.all()
    data = {'todo_items': []}
    for todo_item in todo_items:
        data['todo_items'].append(todo_item.todo_text)
    print(data)
    return JsonResponse(data)


def savetodo(request):
    data = json.loads(request.body)
    todo_text = data['todo_text']

    todo_item = TodoItem(todo_text=todo_text, completed=False)
    todo_item.save()

    return HttpResponse('OK')



