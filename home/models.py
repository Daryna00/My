from django.db import models
from merchan.models import Merchandise
from django.contrib.auth.models import User

"""
class Comment(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField(max_length=2048)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return f'Comment- {self.name}'

    class Meta:
        ordering = ['-timestamp', '-updated']"""

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    merchan = models.ForeignKey(Merchandise, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'User {self.customer.id} - {self.merchan.name} - {self.count}'
# Create your models here.
