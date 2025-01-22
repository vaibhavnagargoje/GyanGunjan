from django.db import models

# Create your models here.


class Contribute(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    subscribed = models.BooleanField(default=False)
    message = models.TextField()
    is_approved = models.BooleanField(default=False)
    

    # File fields for different media types
    photo = models.ImageField(upload_to='Contribute/Photos/', null=True, blank=True)
    video = models.FileField(upload_to='Contribute/Videos/', null=True, blank=True)
    pdf = models.FileField(upload_to='Contribute/PDFs/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name})"

