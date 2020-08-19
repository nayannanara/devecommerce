from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.views.generic import TemplateView, View, CreateView
from core.models import Contato
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()


class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()

class ContactView(object):

    def __call__(self, request):
        success = False
        if request.method == 'POST':
            contato = {}
            contato['nome'] = request.POST.get('nome')
            contato['telefone'] = request.POST.get('telefone')
            contato['email'] = request.POST.get('email')
            contato['mensagem'] = request.POST.get('mensagem')

            Contato.objects.create(**contato)
            success = True
        elif request.method == 'POST':
            messages.error(request, 'Formulário inválido')
        context = {
            'success': success
        }
        return render(request, 'contact.html', context)
        

contact = ContactView()


def contact2(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, '_contact.html', context)  