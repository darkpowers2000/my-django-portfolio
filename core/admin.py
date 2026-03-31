from django.contrib import admin
from .models import Service, ContactMessage, AboutMe

admin.site.register(Service)
admin.site.register(ContactMessage)
admin.site.register(AboutMe)