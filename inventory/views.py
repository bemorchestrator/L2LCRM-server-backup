# inventory/views.py

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_protect
def product_list(request):
    """
    View to display the list of products.
    """
    products = Product.objects.all()
    form = ProductForm()
    return render(request, 'inventory/product_list.html', {'products': products, 'form': form})


def add_product(request):
    """
    View to handle adding a new product.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been successfully added!')
            return redirect('product_list')  # Replace with your actual URL name
        else:
            messages.error(request, 'There was an error adding the product. Please try again.')
            return redirect('product_list')  # Redirecting to the same page to display errors
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})


@require_POST
def delete_product(request, product_id):
    """
    View to delete a single product via AJAX.
    """
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return JsonResponse({'status': 'success'})
    else:
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return redirect('product_list')  # Replace with your actual product list URL name


@require_POST
def bulk_delete_products(request):
    """
    View to delete multiple products via AJAX.
    """
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
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
            'supplier': product.supplier,
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
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        product = get_object_or_404(Product, id=product_id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            updated_product = Product.objects.get(id=product_id)
            data = {
                'id': updated_product.id,
                'item_name': updated_product.item_name,
                'supplier': updated_product.supplier,
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
            # Return form errors
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'message': 'There were errors in the form.', 'errors': errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
