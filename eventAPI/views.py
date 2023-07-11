from django.shortcuts import render
from rest_framework import generics

from .models import Event, Ticket, Order
from .serializers import EventSerializer

class EventAPIView(generics.ListCreateAPIView):
    
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    read_only_fields = ('organizer', 'id')

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class EventAPIRetrieveUpdateDeleteDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer