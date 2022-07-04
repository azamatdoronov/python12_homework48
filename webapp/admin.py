from django.contrib import admin

from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'p_name', 'description', 'balance', 'price', 'created_time', 'updated_time']
    list_display_links = ['p_name']
    list_filter = ['category']
    search_fields = ['p_name']
    fields = ['p_name', 'category', 'balance', 'price', 'created_time', 'updated_time']
    readonly_fields = ['created_time', 'updated_time']


admin.site.register(Product, ProductAdmin)
