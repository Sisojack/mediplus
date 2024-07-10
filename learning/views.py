from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def notfound(request):
    return render(request, '404.html')
def blog(request):
    return render(request, 'blog-single.html')
def contact(request):
    return render(request, 'contact.html')
def portfolio(request):
    return render(request, 'portfolio-details.html')
def ipnav(request):
    return render(request, '#')
