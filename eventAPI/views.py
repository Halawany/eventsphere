from django.shortcuts import render
from rest_framework import generics

from .models import Event, Ticket, Order
from .serializers import EventSerializer, TicketSerializer, OrderSerializer

class EventAPIView(generics.ListCreateAPIView):
    
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    read_only_fields = ('organizer', 'id')

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class EventAPIRetrieveUpdateDeleteDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TicketAPIView(generics.ListCreateAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    read_only_fields = ('id',)

class TicketAPIRetrieveUpdateDeleteDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class OrderAPIView(generics.ListCreateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    read_only_fields = ('id', 'owner', 'ticket','ticket_price', 'total_price')

    def perform_create(self, serializer):
        ticket_id = self.request.data.get('ticket')
        ticket = Ticket.objects.get(id=ticket_id)
        event = ticket.event
        serializer.validated_data['event'] = event
        serializer.save(owner=self.request.user, event=event)

class OrderAPIRetrieveUpdateDeleteDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

