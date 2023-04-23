from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages.

def homepage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(email=email, subject=subject,
                          message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request, 'home.html')
