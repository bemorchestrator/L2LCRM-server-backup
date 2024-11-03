# patients/forms.py

from django import forms
from .models import Patients

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = [
            'patient_no',
            'first_name',
            'last_name',
            'birth_date',
            'nric',
            'country',
            'address',
            'phone',
            'fax',
            'email',
            'consented',
            'remarks',
            'active',
            'profile_photo'  # Added profile_photo
        ]
        widgets = {
            'patient_no': forms.TextInput(attrs={
                'placeholder': 'Patient No',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'birth_date': forms.DateInput(attrs={
                'placeholder': 'Birth Date',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white',
                'type': 'date'  # Ensures date picker in browsers
            }),
            'nric': forms.TextInput(attrs={
                'placeholder': 'NRIC',
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
            'consented': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-primary-600 border-gray-300 rounded focus:ring-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'remarks': forms.Textarea(attrs={
                'placeholder': 'Remarks',
                'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:text-white',
                'rows': 3
            }),
            'active': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-primary-600 border-gray-300 rounded focus:ring-primary-500 dark:bg-gray-700 dark:text-white'
            }),
            'profile_photo': forms.ClearableFileInput(attrs={  # Added widget for profile_photo
                'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        # Customize initialization if needed
