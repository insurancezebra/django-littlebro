from django.db import models

class Event(models.Model):
    """
    Dummy model for development.
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    event = models.SlugField()
    params = models.TextField()