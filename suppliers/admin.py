# suppliers/admin.py

from django.contrib import admin
from .models import Supplier

class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'supplier_no', 
        'supplier_name', 
        'contact', 
        'country', 
        'phone', 
        'email', 
        'active', 
        'updated', 
        'created'
    )
    list_filter = ('active', 'country')
    search_fields = ('supplier_no', 'supplier_name', 'contact', 'email', 'phone')
    ordering = ('supplier_name',)
    readonly_fields = ('updated', 'created')
    fieldsets = (
        (None, {
            'fields': (
                'supplier_no', 
                'supplier_name', 
                'contact', 
                'country', 
                'address', 
                'phone', 
                'fax', 
                'email', 
                'staff_in_charge', 
                'remarks', 
                'active'
            )
        }),
        ('Timestamps', {
            'fields': ('updated', 'created'),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Supplier, SupplierAdmin)
