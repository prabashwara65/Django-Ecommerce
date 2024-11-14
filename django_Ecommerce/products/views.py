from django.shortcuts import render, get_object_or_404

# Import your models
from .models import Category, Product

# View to list products
def product_list(request, category_slug=None):
    category = None
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'products/product/list.html', {
        'category': category,
        'products': products,
        'categories': categories,
    })

# View for product details
def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'products/product/detail.html', {
        'product': product,
    })
