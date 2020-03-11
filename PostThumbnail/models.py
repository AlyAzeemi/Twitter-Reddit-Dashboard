from django.db import models

# Create your models here.

class PostWindow(models.Model):
    image_path= models.TextField(default=None, unique=True)
    post_link= models.TextField()
    
    def __str__(self):
        if self.post_link:
            return self.post_link
        return None

