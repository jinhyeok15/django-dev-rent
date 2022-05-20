from django.db import models
from .validators import validate_title_content


# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=50, validators=[validate_title_content])
    content = models.TextField()
    dt_created = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
