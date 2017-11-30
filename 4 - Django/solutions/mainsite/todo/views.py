from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import TodoItem

def index(request):

    # print(request.method)
    # print(request.body)
    # print(request.GET)

    # name = request.GET['name']
    # print(name)
    #
    #
    # output = '<html><head></head><body>'
    # output += '<ul>'
    # for i in range(100):
    #     output += f'<li>{i}</li>'
    # output += '</body></html>'
    #
    # return HttpResponse(output)

    # todo_items = TodoItem.objects.all()
    #
    # output = '<html><head></head><body>'
    # output += '<ul>'
    #
    # for todo_item in todo_items:
    #     #print(todo_item.todo_text)
    #     output += f'<li>{todo_item.todo_text}</li>'
    # output += '</ul>'
    # output += '</body></html>'
    # return HttpResponse(output)


    todo_items = TodoItem.objects.filter(completed=False)
    completed_items = TodoItem.objects.filter(completed=True)

    context = {'todo_items': todo_items,
               'completed_items': completed_items}
    return render(request, 'todo/index.html', context)


def savetodo(request):

    todo_text = request.POST['todo_text']

    print(reverse('todo:index'))

    todo_item = TodoItem(todo_text=todo_text)
    todo_item.save()

    return HttpResponseRedirect(reverse('todo:index'))

def completetodo(request):
    todo_id = request.POST['todo_id']
    todo_item = TodoItem.objects.get(pk=todo_id)
    todo_item.completed = True
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))
