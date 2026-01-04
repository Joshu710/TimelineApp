from django.db import models

# Create your models here.
class Event(models.Model):
    date = models.DateField()
    title = models.CharField()
    description = models.CharField(null=True,blank=True)

def event_image_path(instance, filename):

    event_date = instance.event.date
    date_parts = event_date.split('-')
    return f"images/{date_parts[0]}/{date_parts[1]}/{date_parts[2]}/{filename}"

class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=event_image_path)
    



