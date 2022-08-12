from django.db import models

# Create your models here.

class EventData(models.Model):
    content = models.CharField(max_length=1000, default="")
    date = models.DateTimeField()
    image = models.ImageField()

    def __str__(self):
        return self.content[:len(self.content) if len(self.content)<15 else 15]
