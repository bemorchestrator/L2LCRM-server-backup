# suppliers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier_list, name='supplier_list'),
    path('add/', views.add_supplier, name='add_supplier'),
    path('delete/<int:supplier_id>/', views.delete_supplier, name='delete_supplier'),
    path('bulk_delete/', views.bulk_delete_suppliers, name='bulk_delete_suppliers'),
    path('edit/<int:supplier_id>/', views.edit_supplier, name='edit_supplier'),
    path('update/<int:supplier_id>/', views.update_supplier, name='update_supplier'),
    path('search_suppliers/', views.search_suppliers, name='search_suppliers'),
]
