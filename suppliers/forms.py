# suppliers/forms.py

from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    """
    Form to create or update a supplier with all relevant details.
    """
    class Meta:
        model = Supplier
        fields = [
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
        ]
        widgets = {
            'supplier_no': forms.TextInput(attrs={
                'placeholder': 'Supplier Number',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'supplier_name': forms.TextInput(attrs={
                'placeholder': 'Supplier Name',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'contact': forms.TextInput(attrs={
                'placeholder': 'Contact Person',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Country',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Address',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white',
                'rows': 3
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'fax': forms.TextInput(attrs={
                'placeholder': 'Fax',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'staff_in_charge': forms.TextInput(attrs={
                'placeholder': 'Staff In Charge',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'remarks': forms.Textarea(attrs={
                'placeholder': 'Remarks',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white',
                'rows': 3
            }),
            'active': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-4 w-4 text-primary-600'
            }),
        }
