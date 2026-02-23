from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world!"
    context = {"name": name}
    return render(request, "bookmodule/index.html", context)
