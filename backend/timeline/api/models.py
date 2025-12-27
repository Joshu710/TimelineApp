from django.db import models

# Create your models here.
class Event(models.Model):
    date = models.DateField()
    title = models.CharField()
    description = models.CharField(null=True,blank=True)

class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    

