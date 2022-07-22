from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.

def get_deadline():
    return datetime.today() + timedelta(days=1)

class Task(models.Model):
 
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
  start = models.DateTimeField(default=timezone.now)
  end = models.DateTimeField(default=get_deadline)

      
  def __str__(self):
    return self.title