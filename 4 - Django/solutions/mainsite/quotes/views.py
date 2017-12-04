from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Quote

def index(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/index.html', {'quotes': quotes})


def savequote(request):
    body = request.POST['quote_body']
    author = request.POST['quote_author']
    quote = Quote(body=body, author=author)
    quote.save()

    return HttpResponseRedirect(reverse('quotes:index'))


