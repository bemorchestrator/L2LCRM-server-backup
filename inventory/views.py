# inventory/views.py

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def product_list(request):
    """
    View to display the list of products.
    """
    products = Product.objects.all().select_related('supplier')  # Optimize query with select_related
    form = ProductForm()
    return render(request, 'inventory/product_list.html', {'products': products, 'form': form})


def add_product(request):
    """
    View to handle adding a new product.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Prepare product data to send back
                product_data = {
                    'id': product.id,
                    'item_name': product.item_name,
                    'quantity': product.quantity,
                    'supplier_id': product.supplier.id,
                    'supplier_name': product.supplier.supplier_name,
                    'currency_code': product.currency_code,
                    'retail_price': str(product.retail_price),
                    'uom': product.uom,
                    'discountable_all': 'Yes' if product.discountable_all else 'No',
                    'discountable_members': 'Yes' if product.discountable_members else 'No',
                    'active': 'Yes' if product.active else 'No',
                    'photo_url': product.photo.url if product.photo else '',
                }
                return JsonResponse({'status': 'success', 'message': 'Product added successfully!', 'product': product_data})
            else:
                messages.success(request, 'Product has been successfully added!')
                return redirect('product_list')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({'status': 'error', 'errors': errors})
            else:
                messages.error(request, 'There was an error adding the product. Please try again.')
                return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})


@require_POST
def delete_product(request, product_id):
    """
    View to delete a single product via AJAX or non-AJAX request.
    """
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return JsonResponse({'status': 'success'})
    else:
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        messages.success(request, 'Product has been successfully deleted.')
        return redirect('product_list')


@require_POST
def bulk_delete_products(request):
    """
    View to delete multiple products via AJAX.
    """
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        product_ids = request.POST.getlist('product_ids')
        if product_ids:
            Product.objects.filter(id__in=product_ids).delete()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No products selected.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def edit_product(request, product_id):
    """
    View to fetch product data for editing via AJAX.
    """
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        product = get_object_or_404(Product, id=product_id)
        data = {
            'id': product.id,
            'item_name': product.item_name,
            'quantity': product.quantity,
            'supplier_id': product.supplier.id,
            'supplier_name': product.supplier.supplier_name,
            'currency_code': product.currency_code,
            'retail_price': str(product.retail_price) if product.retail_price else '',
            'uom': product.uom,
            'discountable_all': bool(product.discountable_all),
            'discountable_members': bool(product.discountable_members),
            'active': bool(product.active),
            'photo_url': product.photo.url if product.photo else '',
        }
        return JsonResponse({'status': 'success', 'product': data})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


@require_POST
def update_product(request, product_id):
    """
    View to update a product via AJAX.
    """
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        product = get_object_or_404(Product, id=product_id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            updated_product = Product.objects.select_related('supplier').get(id=product_id)
            data = {
                'id': updated_product.id,
                'item_name': updated_product.item_name,
                'quantity': updated_product.quantity,
                'supplier_id': updated_product.supplier.id,
                'supplier_name': updated_product.supplier.supplier_name,
                'currency_code': updated_product.currency_code,
                'retail_price': str(updated_product.retail_price),
                'uom': updated_product.uom,
                'discountable_all': 'Yes' if updated_product.discountable_all else 'No',
                'discountable_members': 'Yes' if updated_product.discountable_members else 'No',
                'active': 'Yes' if updated_product.active else 'No',
                'photo_url': updated_product.photo.url if updated_product.photo else '',
            }
            return JsonResponse({'status': 'success', 'message': 'Product updated successfully!', 'product': data})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'message': 'There were errors in the form.', 'errors': errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
