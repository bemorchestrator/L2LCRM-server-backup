from django.urls import path
from .views import product_list, add_product, delete_product, bulk_delete_products

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/add/', add_product, name='add_product'),
    path('product/delete/<int:product_id>/', delete_product, name='delete_product'),
    path('product/bulk_delete/', bulk_delete_products, name='bulk_delete_products'),
]
