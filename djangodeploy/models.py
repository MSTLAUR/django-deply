from django.db import models

class Lead(models.Model):
    first_name = models.CharField(max_length=50,  blank=True, null=True)
    last_name = models.CharField(max_length=50,  blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.email}"