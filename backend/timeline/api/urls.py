from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, add_event, EventPhotoViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'eventphotos', EventPhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add_event/', add_event, name='add_event'),
]
