from django.shortcuts import render
from django.views import generic
from catalog.models import Book,Author,BookInstance,Genre
# Create your views here.
def index(request):

    """View function for home page """

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available Books with status a
    num_instances_available = BookInstance.objects.filter(status = 'a').count()

    #The 'all()' implied by default
    num_authors = Author.objects.count()

    context = {
    'num_books':num_books,
    'num_instances':num_instances,
    'num_instances_available':num_instances_available,
    'num_authors':num_authors
    }

    # Render HTML Template to index.HTML

    return render(request,'catalog/index.html',context =context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list' # Name for the list template variable
    # queryset = Book.objects.filter(title__icontains = 'War'[:5])
    template_name = 'catlog/my_book_list.html'
    print(context_object_name)
class BookDetailView(generic.DetailView):
    model = Book

def book_detail_view(request,primary_key):
    try:
        book = Book.objects.get(pk = primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does exist')

    return render(request, 'catalog/book_details.html', context ={'book':book})
    
