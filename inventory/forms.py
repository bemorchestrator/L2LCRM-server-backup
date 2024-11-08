# inventory/forms.py

from django import forms
from .models import Product
from suppliers.models import Supplier  

class ProductForm(forms.ModelForm):
    """
    Form to create or update a product with supplier selection as a dropdown.
    """
    class Meta:
        model = Product
        fields = [
            'item_name', 
            'supplier', 
            'currency_code', 
            'retail_price', 
            'uom', 
            'discountable_all', 
            'discountable_members', 
            'active', 
            'photo',
            'quantity'
        ]
        widgets = {
            'item_name': forms.TextInput(attrs={
                'placeholder': 'Item Name',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'supplier': forms.Select(attrs={
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'currency_code': forms.TextInput(attrs={
                'placeholder': 'Currency Code',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'retail_price': forms.NumberInput(attrs={
                'placeholder': 'Retail Price',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'uom': forms.TextInput(attrs={
                'placeholder': 'Unit of Measure (UOM)',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'
            }),
            'discountable_all': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-4 w-4 text-primary-600'
            }),
            'discountable_members': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-4 w-4 text-primary-600'
            }),
            'active': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-4 w-4 text-primary-600'
            }),
            'quantity': forms.NumberInput(attrs={
                'placeholder': 'Quantity',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Populate the supplier dropdown with only active suppliers
        self.fields['supplier'].queryset = Supplier.objects.filter(active=True)
