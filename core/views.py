from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.views.generic import TemplateView


class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()


def contact(request):
    return render(request, 'contact.html')


def contact(request):
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
