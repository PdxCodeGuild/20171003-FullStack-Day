from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contactapp/index.html', {'contacts': contacts})

def savecontact(request):
    contact_name = request.POST['contact_name']
    contact_fruit = request.POST['contact_fruit']
    contact_color = request.POST['contact_color']

    contact = Contact(name=contact_name, fruit=contact_fruit, color=contact_color)
    contact.save()

    return HttpResponseRedirect(reverse('contactapp:index'))


