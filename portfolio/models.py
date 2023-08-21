from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="portfolio")
    title = models.CharField(max_length=255)
    description = models.TextField()
    client = models.CharField(max_length=20)
    platform = models.CharField(max_length=20, default="Fiverr")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="images/")
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption
