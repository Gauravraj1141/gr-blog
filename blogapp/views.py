from django.shortcuts import render,HttpResponse

# Create your views here.
def run(request):
    return HttpResponse("it is blog")