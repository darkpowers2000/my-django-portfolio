from django.shortcuts import render, redirect
from .models import Service, ContactMessage, AboutMe

def home(request):
    services = Service.objects.all()
    about = AboutMe.objects.first()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        return redirect('home')

    return render(request, 'core/home.html', {'services': services, 'about': about})
