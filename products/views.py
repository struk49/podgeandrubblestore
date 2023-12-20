# Code adapted from the CI Boutique Ado mini project

from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import (
    Product, Gender, Category, SubCategory, ProductType)



def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()
    sort = None
    direction = None
    query = None
    gender = None
    category = None
    sub_category = None
    product_type = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            products = products.filter(
                gender__name__in=gender)
            gender = Gender.objects.filter(
                name__in=gender)

        if 'category' in request.GET:
            category = request.GET['category'].split(',')
            products = products.filter(
                category__name__in=category)
            category = Category.objects.filter(
                name__in=category)

        if 'sub_category' in request.GET:
            sub_category = request.GET['sub_category'].split(',')
            products = products.filter(
                sub_category__name__in=sub_category)
            sub_category = SubCategory.objects.filter(
                name__in=sub_category)

        if 'product_type' in request.GET:
            product_type = request.GET['product_type'].split(',')
            products = products.filter(
                product_type__name__in=product_type)
            product_type = ProductType.objects.filter(
                name__in=product_type)

       

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a seearch criteria")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) |
                Q(product_description__icontains=query) |
                Q(gender__name__icontains=query) |
                Q(category__name__icontains=query) |
                Q(sub_category__name__icontains=query) |
                Q(product_type__name__icontains=query))
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'search_term': query,
        'current_gender': gender,
        'current_category': category,
        'current_sub_category': sub_category,
        'current_product_type': product_type,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


