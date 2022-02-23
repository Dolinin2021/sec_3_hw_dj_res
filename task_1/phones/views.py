from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


SORT_MAP = {
    'name': 'name',
    'min_price': 'price',
    'max_price': '-price',
}


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort')
    if sorting:
        sort_fields = Phone.objects.order_by(SORT_MAP[sorting])
        context = {'phones': sort_fields}
        return render(request, template, context)
    else:
        catalog_objects = Phone.objects.all()
        context = {'phones': catalog_objects}
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone = Phone.objects.get(slug=slug)
        print(phone)
        context = {'phone': phone}
        return render(request, template, context)
    except Phone.DoesNotExist:
        return HttpResponse('Телефон не найден. \n'
                            'Проверьте введенные данные и попробуйте еще раз.')