from django.shortcuts import render, redirect
from .models import Service, ContactMessage

def home(request):
    services = Service.objects.all()
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        return redirect('home')

    return render(request, 'core/home.html', {'services': services})
