from django.shortcuts import render
from django.http import HttpResponse   # لو لسه تحتاجين index2، وإلا تقدرين تحذفينه

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

