# suppliers/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from .models import Supplier
from .forms import SupplierForm

@csrf_protect
def supplier_list(request):
    """
    View to display the list of suppliers.
    """
    suppliers = Supplier.objects.all()  # Fetch all suppliers
    form = SupplierForm()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers, 'form': form})

def add_supplier(request):
    """
    View to handle form submission for adding a new supplier.
    If the request is AJAX, it returns a JSON response; otherwise, it redirects.
    """
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            supplier = form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Prepare supplier data to send back
                supplier_data = {
                    'id': supplier.id,
                    'supplier_no': supplier.supplier_no,
                    'supplier_name': supplier.supplier_name,
                    'contact': supplier.contact,
                    'country': supplier.country,
                    'phone': supplier.phone,
                    'email': supplier.email,
                    'active': 'Yes' if supplier.active else 'No',
                }
                return JsonResponse({'status': 'success', 'message': 'Supplier added successfully!', 'supplier': supplier_data})
            else:
                messages.success(request, 'Supplier has been successfully added!')
                return redirect('supplier_list')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({'status': 'error', 'errors': errors})
            else:
                messages.error(request, 'There was an error adding the supplier. Please try again.')
                return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'suppliers/supplier_form.html', {'form': form})  # Separate template for non-AJAX form submission

@require_POST
def delete_supplier(request, supplier_id):
    """
    View to delete a single supplier via AJAX or non-AJAX request.
    """
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        supplier = get_object_or_404(Supplier, id=supplier_id)
        supplier.delete()
        return JsonResponse({'status': 'success', 'message': 'Supplier deleted successfully.'})
    else:
        supplier = get_object_or_404(Supplier, id=supplier_id)
        supplier.delete()
        messages.success(request, 'Supplier has been successfully deleted.')
        return redirect('supplier_list')

@require_POST
def bulk_delete_suppliers(request):
    """
    View to delete multiple suppliers via AJAX.
    """
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        supplier_ids = request.POST.getlist('supplier_ids')
        if supplier_ids:
            Supplier.objects.filter(id__in=supplier_ids).delete()
            return JsonResponse({'status': 'success', 'message': 'Selected suppliers have been deleted.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No suppliers selected.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def edit_supplier(request, supplier_id):
    """
    View to fetch supplier data for editing via AJAX or handle form submission.
    """
    supplier = get_object_or_404(Supplier, id=supplier_id)

    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Prepare updated supplier data to send back
                updated_supplier = Supplier.objects.get(id=supplier_id)
                supplier_data = {
                    'id': updated_supplier.id,
                    'supplier_no': updated_supplier.supplier_no,
                    'supplier_name': updated_supplier.supplier_name,
                    'contact': updated_supplier.contact,
                    'country': updated_supplier.country,
                    'phone': updated_supplier.phone,
                    'email': updated_supplier.email,
                    'active': 'Yes' if updated_supplier.active else 'No',
                }
                return JsonResponse({'status': 'success', 'message': 'Supplier updated successfully!', 'supplier': supplier_data})
            else:
                messages.success(request, 'Supplier has been successfully updated!')
                return redirect('supplier_list')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({'status': 'error', 'errors': errors})
            else:
                messages.error(request, 'There was an error updating the supplier. Please try again.')
    else:
        form = SupplierForm(instance=supplier)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Prepare supplier data to send back
        supplier_data = {
            'id': supplier.id,
            'supplier_no': supplier.supplier_no,
            'supplier_name': supplier.supplier_name,
            'contact': supplier.contact,
            'country': supplier.country,
            'phone': supplier.phone,
            'email': supplier.email,
            'active': supplier.active,
        }
        return JsonResponse({'status': 'success', 'supplier': supplier_data})
    else:
        return render(request, 'suppliers/supplier_form.html', {'form': form, 'supplier': supplier})
