from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Book, Genre, Status
from .forms import StatusForm


def home(request):
    return render(request, 'home.html')


def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    genres_book_doesnt_have = Genre.objects.exclude(id__in=book.genres.all().values_list('id'))
    status_form = StatusForm()
    return render(request, 'books/details.html', {
        'book': book,
        'status_form': status_form,
        'genres': genres_book_doesnt_have,
    })


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'year_published']


class BookUpdate(UpdateView):
    model = Book
    fields = ['author', 'description', 'year_published']
    success_url = '/books/'


class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'


def add_status(request, book_id):
    form = StatusForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.book_id = book_id
        new_status.save()
    return redirect('book-detail', book_id=book_id)


class GenreCreate(CreateView):
    model = Genre
    fields = '__all__'


class GenreList(ListView):
    model = Genre


class GenreDetail(DetailView):
    model = Genre


class GenreUpdate(UpdateView):
    model = Genre
    fields = ['name', 'description']


class GenreDelete(DeleteView):
    model = Genre
    success_url = '/genres/'


def associate_genre(request, book_id):
    genre_id = request.POST.get('genre_id')
    Book.objects.get(id=book_id).genres.add(genre_id)
    return redirect('book-detail', book_id=book_id)


def remove_genre(request, book_id, genre_id):
    Book.objects.get(id=book_id).genres.remove(genre_id)
    return redirect('book-detail', book_id=book_id)
