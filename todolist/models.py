from django.db import models
from datetime import datetime
from .models import TodoListItem 
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    
    def __str__(self):
        return self.title

