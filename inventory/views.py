from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Adjust the redirect as needed
    else:
        form = ProductForm()
    return render(request, 'inventory/product_list.html', {'products': products, 'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list after saving
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def delete_product(request, product_id):
    """View to delete a single product"""
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_list')  # Replace with your actual product list URL name

def bulk_delete_products(request):
    """View to delete multiple products"""
    if request.method == "POST":
        product_ids = request.POST.getlist('product_ids')
        Product.objects.filter(id__in=product_ids).delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})