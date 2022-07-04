from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now=True)
