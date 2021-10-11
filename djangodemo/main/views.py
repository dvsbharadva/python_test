from django.shortcuts import render
from django.http import HttpResponse, request
from main.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        passwd = request.POST.get('passwd')
        addr = request.POST.get('addr')
        city = request.POST.get('city')
        pincode = request.POST.get('zip')
        contact = Contact(email = email, passwd = passwd, addr = addr, city = city, pincode = pincode, date = datetime.today())
        contact.save()
        messages.success(request, "Your record has been saved successfully..")
    return render(request, 'contact.html')

def web(request):
    return render(request, 'web.html')

def cyber(request):
    return render(request, 'cyber.html')

def domain(request):
    return render(request, 'domain.html')

def home(request):
    data = {
        "myName" : "Divyesh",
        "myAge": 28
    }
    messages.success(request, "This is my sample message")
    return render(request, 'index.html', data)
    # return HttpResponse("Welcome to the Home, Divyesh")
    