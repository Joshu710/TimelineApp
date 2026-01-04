from django.shortcuts import render
from .models import Event, EventPhoto
from .serializers import EventSerializer, EventPhotoSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer 


class EventPhotoViewSet(viewsets.ModelViewSet):
    queryset = EventPhoto.objects.all()
    serializer_class = EventPhotoSerializer 

@api_view(['POST'])
def add_event(request):
    print(request)

    new_event = Event.objects.create(
        date=request.data["date"],
        title=request.data["name"],
        description=request.data["desc"]
    )

    photos = request.FILES.getlist('photos[]')  

    for photo in photos:
        new_event_photo = EventPhoto.objects.create(
            event=new_event,
            image=photo
        )

    return Response({"data": 'Event added successfully'})