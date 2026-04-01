from django.shortcuts import render, redirect
from .models import Service, ContactMessage, AboutMe, Project

def home(request):
    services = Service.objects.all()
    about = AboutMe.objects.first()
    projects = Project.objects.all()


    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        return redirect('home')

    return render(request, 'core/home.html', {'services': services, 'about': about, 'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'core/project_detail.html', {'project': project})