from django.shortcuts import render
from django.http import HttpResponse   # إذا كنتِ لا زلتِ تستخدمينه لـ index2

def index(request):
    name = request.GET.get("name") or "world!"
    context = {"name": name}
    return render(request, "bookmodule/index.html", context)

def index2(request, val1=0):
    return HttpResponse("value1 " + str(val1))

def viewbook(request, bookId):
    book1 = {
        "id": 123,
        "title": "Continuous Delivery",
        "author": "J. Humble and D. Farley",
    }
    book2 = {
        "id": 456,
        "title": "Secrets of Reverse Engineering",
        "author": "E. Eilam",
    }

    targetBook = None
    if book1["id"] == bookId:
        targetBook = book1
    if book2["id"] == bookId:
        targetBook = book2

    context = {"book": targetBook}   # 'book' هو الاسم اللي راح نستخدمه في القالب
    return render(request, "bookmodule/show.html", context)
