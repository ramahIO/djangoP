from django.http import HttpResponse
def index(request):
 name = request.GET.get("name") or "Ramah!" 
 return HttpResponse("Hello, "+ name) 
