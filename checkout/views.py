# coding=utf-8

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import RedirectView, TemplateView, ListView, DetailView
from django.forms import modelformset_factory
from django.contrib import messages
from django.urls  import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product
from django.conf import settings
#from pagseguro import PagSeguro

#from paypal.standard.forms import PayPalPaymentsForm
#from paypal.standard.models import ST_PP_COMPLETED
#from paypal.standard.ipn.signals import valid_ipn_received

from .models import CartItem
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class CreateCartItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CartItem.objects.add_item(
            self.request.session.session_key, product
        )
        if created:
            messages.success(self.request, 'Produto adicionado com sucesso')
        else:
            messages.success(self.request, 'Produto atualizado com sucesso')
        return reverse('checkout:cart_item')



class CartItemView(TemplateView):

    template_name = 'checkout/cart.html'

    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(
            CartItem, fields=('quantity',), can_delete=True, extra=0
        )
        session_key = self.request.session.session_key
        if session_key:
            if clear:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key)
                )
            else:
                formset = CartItemFormSet(
                    queryset=CartItem.objects.filter(cart_key=session_key),
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=CartItem.objects.none())
        return formset

    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context

    def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Carrinho atualizado com sucesso')
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)



class CheckoutView(LoginRequiredMixin, TemplateView):

        template_name = 'checkout/checkout.html'

        def get(self, request, *args, **kwargs):
            session_key = request.session.session_key
            if session_key and CartItem.objects.filter(cart_key=session_key).exists():
                if session_key and CartItem.objects.filter(cart_key=session_key).exists():
                    cart_items = CartItem.objects.filter(cart_key=session_key)
                    order = Order.object.create_order(
                    user=request.user, cart_items=cart_items
                )
                cart_items.delete()
            else:
                messages.info(request, 'Não há itens no carrinho de compras')
                return redirect('checkout:cart_item')
            response = super(CheckoutView, self).get(request, *args, **kwargs)
            response.context_data['order'] = order
            return response        


create_cartitem = CreateCartItemView.as_view()
cart_item = CartItemView.as_view()
checkout = CheckoutView.as_view()