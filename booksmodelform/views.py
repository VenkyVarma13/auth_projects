from django.shortcuts import render
from .forms import BooksForm
from .models import BooksModel


# Create your views here.

def index_view(request):
    return render(request, 'index.html')


def add_books(request):
    form = BooksForm()
    print("Hello")
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request, 'addbook.html', {'form': form})


def list_books_view(request):
    books = BooksModel.objects.all()
    return render(request, 'listbook.html', {'books_list': books})
