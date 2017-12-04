from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Quote
import json

def index(request):

    quotes = Quote.objects.all()

    # output = []
    # for quote in Quote.objects.all():
    #     author_id = quote.author_id
    #     author = Author.objects.get(pk=author_id)
    #     output.append({'quote': quote.body, 'author': author.name})

    return render(request, 'quotes2/index.html', {'quotes':quotes})

def savequote(request):
    data = json.loads(request.body)
    quote_body = data['quote_body']
    quote_author = data['quote_author']

    author = None
    if (Author.objects.filter(name=quote_author).exists()):
        author = Author.objects.get(name=quote_author)
    else:
        author = Author(name=quote_author)
        author.save()

    quote = Quote(body=quote_body, author=author)
    quote.save()

    return HttpResponse('OK')

