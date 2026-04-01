from django.contrib import admin
from .models import Service, ContactMessage, AboutMe, Project

admin.site.register(Service)
admin.site.register(ContactMessage)
admin.site.register(AboutMe)
admin.site.register(Project)