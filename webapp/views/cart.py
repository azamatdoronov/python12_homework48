from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from webapp.forms import CartForm, OrderForm
from webapp.models import Cart, Product, Order, OrderProduct


class CartAddView(CreateView):
    model = Cart
    form_class = CartForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        qty = form.cleaned_data.get("qty")
        if qty > product.balance:
            return HttpResponseBadRequest(
                f"Такое количество товара {product.p_name} всего {product.balance}. Добавить {qty} штук не представляется возможным")
        else:
            cart_product, is_created = Cart.objects.get_or_create(product=product)
            if is_created:
                cart_product.qty = qty
            else:
                cart_product.qty += qty
            cart_product.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        next = self.request.GET.get("next")
        if next:
            return next
        return reverse("webapp:index")


class CartView(ListView):
    model = Cart
    template_name = "cart/cart_view.html"
    context_object_name = "cart"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['total'] = Cart.get_total()
        context['form'] = OrderForm()
        return context


class CartDeleteView(DeleteView):
    model = Cart
    success_url = reverse_lazy('webapp:cart')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class CartDeleteOneView(DeleteView):
    model = Cart
    success_url = reverse_lazy('webapp:cart')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        cart = self.object
        cart.qty -= 1
        if cart.qty < 1:
            cart.delete()
        else:
            cart.save()
        return HttpResponseRedirect(success_url)