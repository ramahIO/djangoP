from django.http import HttpResponse
def index(request):
 name = request.GET.get("name") or "Ramah!"
 return HttpResponse("Hello, "+name)
def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))
