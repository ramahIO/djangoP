from django.shortcuts import render
from django.http import HttpResponse   # لو لسه تحتاجين index2، وإلا تقدرين تحذفينه
from .models import Book

# لو لسه تبين تحتفظين بـ index2 من لاب 3:
def index2(request, val1=0):
    return HttpResponse("value1 " + str(val1))


# صفحات لاب 4

def index(request):
    return render(request, 'bookmodule/index.html')

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, "bookmodule/listing.html")

def tables(request):
    return render(request, "bookmodule/tables.html")

def searchBooks(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True

            if contained: newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Domian ', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765, 'title':'accompanying minister', 'author':'gazi alqusibi'}
    book3 = {'id':43211234, 'title':'1001 night', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


def insertBooks(request):
    Book.objects.create(title='Domian', author='J.Humble and D. Farley', price=120.00)
    Book.objects.create(title='accompanying minister', author='gazi alqusibi', price=97.00)
    Book.objects.create(title='1001 night', author='Andriy Burkov', price=100.00)
    return render(request, 'bookmodule/bookList.html', {'books': Book.objects.all()})

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='night')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
                          .filter(title__icontains='minister')\
                          .filter(edition__gte=2)\
                          .exclude(price__lte=50)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    


def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': books})


from django.db.models import Q


def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gte=1) & 
        (Q(title__icontains='or') | Q(author__icontains='or'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & 
        ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})



def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})



from django.db.models import Count, Sum, Avg, Max, Min

def lab8_task5(request):
    data = Book.objects.aggregate(
        total_books  = Count('id'),
        total_price  = Sum('price'),
        avg_price    = Avg('price'),
        max_price    = Max('price'),
        min_price    = Min('price'),
    )
    return render(request, 'bookmodule/task5.html', {'data': data})


from .models import Book, Address, Student
from django.db.models import Count

def lab8_task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'cities': cities})