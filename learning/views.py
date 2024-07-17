from django.shortcuts import render
from .models import Appointment

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
def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        date = request.POST.get('date')
        message = request.POST.get('message')

        saveappointment = Appointment(name=name, email=email, phone=phone, department=department, doctor=doctor, date=date, message=message)
        saveappointment.save()
