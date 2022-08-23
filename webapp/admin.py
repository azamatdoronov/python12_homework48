from django.contrib import admin

# Register your models here.
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'p_name', 'balance', 'price')
    list_display_links = ('pk', 'p_name')
    list_filter = ('category',)
    search_fields = ('p_name',)


admin.site.register(Product, ProductAdmin)
