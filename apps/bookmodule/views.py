from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html")


def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))
