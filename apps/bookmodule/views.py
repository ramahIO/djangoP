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
    

from django.db.models import Q

def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': books})




def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & 
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

#10
def p1_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/p1_listbooks.html', {'books': books})

from django.shortcuts import render, redirect
def p1_addbook(request):
    if request.method == 'POST':
        title   = request.POST.get('title')
        author  = request.POST.get('author')
        price   = request.POST.get('price')
        edition = request.POST.get('edition')
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('/lab9_part1/listbooks')
    return render(request, 'bookmodule/p1_addbook.html')

def p1_editbook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title   = request.POST.get('title')
        book.author  = request.POST.get('author')
        book.price   = request.POST.get('price')
        book.edition = request.POST.get('edition')
        book.save()
        return redirect('/lab9_part1/listbooks')
    return render(request, 'bookmodule/p1_editbook.html', {'book': book})


def p1_deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/lab9_part1/listbooks')


from .forms import BookForm

def p2_listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/p2_listbooks.html', {'books': books})

def p2_addbook(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/lab9_part2/listbooks')
    return render(request, 'bookmodule/p2_addbook.html', {'form': form})

def p2_editbook(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/lab9_part2/listbooks')
    return render(request, 'bookmodule/p2_editbook.html', {'form': form})

def p2_deletebook(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/lab9_part2/listbooks')

from django.contrib.auth.decorators import login_required
from .models import Student, Address
from .forms import StudentForm, AddressForm
@login_required(login_url='/users/login')
def t1_list(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/t1_list.html', {'students': students})
@login_required(login_url='/users/login')
def t1_add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/lab11/task1/students')
    return render(request, 'bookmodule/t1_form.html', {'form': form, 'title': 'Add Student'})
@login_required(login_url='/users/login')
def t1_edit(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('/lab11/task1/students')
    return render(request, 'bookmodule/t1_form.html', {'form': form, 'title': 'Edit Student'})
@login_required(login_url='/users/login')
def t1_delete(request, id):
    Student.objects.get(id=id).delete()
    return redirect('/lab11/task1/students')


from .models import Student2, Address2
from .forms import Student2Form
@login_required(login_url='/users/login')
def t2_list(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/t2_list.html', {'students': students})

@login_required(login_url='/users/login')
def t2_edit(request, id):
    student = Student2.objects.get(id=id)
    form = Student2Form(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('/lab11/task2/students')
    return render(request, 'bookmodule/t2_form.html', {'form': form, 'title': 'Edit Student'})
@login_required(login_url='/users/login')
def t2_delete(request, id):
    Student2.objects.get(id=id).delete()
    return redirect('/lab11/task2/students')

@login_required(login_url='/users/login')
def t2_add(request):
    if Address2.objects.count() == 0:
        Address2.objects.create(city='Riyadh')
        Address2.objects.create(city='Jeddah')
        Address2.objects.create(city='Hail')
    
    form = Student2Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/lab11/task2/students')
    return render(request, 'bookmodule/t2_form.html', {'form': form, 'title': 'Add Student'})

from .models import Product
from .forms import ProductForm
@login_required(login_url='/users/login')
def t3_list(request):
    products = Product.objects.all()
    return render(request, 'bookmodule/t3_list.html', {'products': products})
@login_required(login_url='/users/login')
def t3_add(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/lab11/task3/products')
    return render(request, 'bookmodule/t3_form.html', {'form': form})