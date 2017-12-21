from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.

def index(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todoapp/index.html', {'todo_items': todo_items})

def addtodo(request):
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))

