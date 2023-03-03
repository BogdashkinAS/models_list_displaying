from django.shortcuts import render
from books.models import Book

def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def show_catalog(request):
    books = Book.objects.all()
    template = 'books.html'
    context = {
        'books': books
    }
    return render(request, template, context)

def show_book(request, date):
    books = Book.objects.filter(pub_date=date)
    template = 'books.html'
    books_list = []
    books_all = Book.objects.order_by('pub_date')
    for book in books_all:
        books_list.append(str(book.pub_date))
    previous_date = 0
    next_date = 0
    stop_date = 1
    prev_date = 0
    n_date = 0
    for date_book in books_list:
        if date == date_book:
            previous_date = books_list.index(date_book) - 1
            if previous_date < 0:
                previous_date = -1
            next_date = books_list.index(date_book) + 1
            if next_date >= len(books_list) - 1:
                next_date = 0
        if date not in books_list:
            print('Нет такой даты')
            stop_date = 0
    for i in books_all:
        if books_list[previous_date] == str(i.pub_date):
            prev_date = i.pub_date
        if books_list[next_date] == str(i.pub_date):
            n_date = i.pub_date

    print(books)
    context = {
        'books': books,
        'previous_date': books_list[previous_date],
        'next_date': books_list[next_date],
        'prev_date': prev_date,
        'n_date': n_date,
        'stop_date': stop_date
    }
    return render(request, template, context)
