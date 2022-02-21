from pprint import pprint

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from books.models import Book


book_object = Book.objects.all()


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': book_object}
    return render(request, template, context)


def selected_book(request, date):
    books = Book.objects.filter(pub_date=date).all()
    pred_date = Book.objects.filter(pub_date__lt=date)
    next_date = Book.objects.filter(pub_date__gt=date)
    template = 'books/select_book.html'
    if pred_date:
        pred_date = pred_date.values('pub_date').first()
    if next_date:
        next_date = next_date.values('pub_date').last()
    context = {'books': books,
               'next_date': pred_date['pub_date'].strftime('%Y-%m-%d') if pred_date else None,
               'pred_date': next_date['pub_date'].strftime('%Y-%m-%d') if next_date else None,
               }
    return render(request, template, context)