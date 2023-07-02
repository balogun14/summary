from django.db import models
from django.utils import timezone
# Create your models here.

class SummaryNotes(models.Model):
    title = models.CharField(max_length=50)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=30, default='ANONYMOUS')
    
    def __str__(self):
        return 'Name:{},ID:{}'.format( self.title, self.id)
    