from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):

    template = 'catalog.html'
    catalog_objects = Phone.objects.all()
    context = {'phones': catalog_objects}
    sorting = request.GET.get('sort')

    if sorting == 'name':
        sort_fields = Phone.objects.order_by('name')
        context = {'phones': sort_fields}
        return render(request, template, context)

    elif sorting == 'min_price':
        sort_fields = Phone.objects.order_by('price')
        context = {'phones': sort_fields}
        return render(request, template, context)

    elif sorting == 'max_price':
        sort_fields = Phone.objects.order_by('-price')
        context = {'phones': sort_fields}
        return render(request, template, context)

    else:
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    print(phone)
    context = {'phone': phone}
    return render(request, template, context)