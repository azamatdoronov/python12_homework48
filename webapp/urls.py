from django.urls import path

from webapp.views import IndexView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView, CartAddView, \
    CartView, CartDeleteView, CartDeleteOneView
from webapp.views.order import OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView

app_name = "webapp"


class OrderProductCreateView:
    pass


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/add-to-cart/', CartAddView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='remove_for_cart'),
    path('cart/<int:pk>/one-delete/', CartDeleteOneView.as_view(), name='remove_one_for_cart'),
    # path('order/create/', OrderCreate.as_view(), name='order_create')
    path('order/', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_view'),
    path('order/create_order/', OrderCreateView.as_view(), name='order_create'),
    path('order/update_order/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
]