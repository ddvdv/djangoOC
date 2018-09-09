from datetime import datetime
from django.shortcuts import render

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date':datetime.now()})

def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    return render(request, 'blog/addition.html', locals())

def base(request):
    return render(request, 'blog/base.html', locals())

from .forms import ContactForm

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        envoi = True

    return render(request, 'blog/contact.html', locals())
