from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    title = models.CharField(max_length=100)
    contact = models.URLField()
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
    rate = models.CharField(blank=True, max_length=25)
    currency = models.CharField(blank=True, max_length=3)
    jd = models.FileField(blank=True)
    active = models.BooleanField(default=True)
    next_step = models.TextField(blank=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
