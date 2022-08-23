from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import OrderForm
from webapp.models import Order


class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'order/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        if self.request.user.has_perm('webapp.oder_view'):
            return Order.objects.all().order_by('-created_at')
        return self.request.user.orders.all().order_by('-created_at')


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_view.html'
    context_object_name = 'order'


class OrderCreateView(PermissionRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_create.html'
    permission_denied_message = "Доступ запрещён"

    def has_permission(self):
        return self.request.user.has_perm("webapp.order_add")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('webapp:order_view', kwargs={'pk': self.object.pk})


class OrderUpdateView(PermissionRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_update.html'
    permission_required = 'webapp.order_update'
    permission_denied_message = "Доступ запрещён"

    def get_success_url(self):
        return reverse('webapp:order_view', kwargs={'pk': self.object.pk})


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('webapp:order_list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

