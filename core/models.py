from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    
    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200, help_text="Example: Python Automation Expert")
    profile_picture = models.ImageField(upload_to='profile/', null=True, blank=True)
    bio = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "About Me"

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='projects/')
    description = models.TextField(help_text="A brief overview of the project.")
    problem_statement = models.TextField(help_text="What business problem were you solving?")
    solution_details = models.TextField(help_text="How did you use Python/Django to solve it?")
    result_roi = models.TextField(help_text="What was the final outcome or time saved?")
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title