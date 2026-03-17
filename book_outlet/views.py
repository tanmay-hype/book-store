from django.shortcuts import get_object_or_404, render
from django.http import Http404
from.models import Book
from book_outlet import models
from django.db.models import Avg

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))["rating__avg"]

    return render(request, "book_outlet/index.html" , 
                   {
                    "total_number_of_books": num_books,
                    "avrage_rating": round(avg_rating, 2) if avg_rating else None,
                    "books": books
                }
            )

def book_detail(request, slug):
   print("views hit", slug)
   book = get_object_or_404(Book, slug=slug)
   return render(request, "book_outlet/book_detail.html" , 
                {
                    #"title": book.title,
                   # "author": book.author,
                    #"rating": book.rating,
                   # "is_bestseller": book.is_bestseller
                    "book": book

                })
