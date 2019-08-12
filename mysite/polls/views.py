from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello World, this page is poll index")
