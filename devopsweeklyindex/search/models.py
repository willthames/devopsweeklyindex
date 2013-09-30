from django.db import models

# Create your models here.
class SearchResult(models.Model):
    link = models.CharField(max_length=256)
    pub_date = models.DateTimeField()
    text = models.CharField(max_length=4096)
