from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView
from webapp.views.base_view import SearchView

from webapp.forms import ProductForm
from webapp.models import Product


class IndexView(SearchView):
    model = Product
    template_name = 'product/index.html'
    ordering = ['category', 'p_name']
    search_fields = ['p_name__icontains']
    paginate_by = 6
    context_object_name = 'products'

    def get_queryset(self):
        return super().get_queryset().filter(balance__gt=0)


class ProductView(DetailView):
    model = Product
    template_name = 'product/product_view.html'
    queryset = Product.objects.filter(balance__gt=0)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return self.request.user.has_perm("webapp.product_create")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return self.request.user.has_perm("webapp.product_update")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('webapp:index')

    def has_permission(self):
        return self.request.user.has_perm("webapp.product_delete")