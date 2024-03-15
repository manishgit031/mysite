from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"mediplus/home.html")
def error(request):
    return render(request,"mediplus/404.html")

def portfolio(request):
    return render(request,"mediplus/fortfolio_detail.html")
def contact(request):
    return render(request,"mediplus/contact.html")
def blog(request):
    return render(request,"mediplus/blog-single.html")
def homee(request):
    return render(request,"mediplus/home.html")