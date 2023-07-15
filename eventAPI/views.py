from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Event, Ticket, Order
from .serializers import EventSerializer, TicketSerializer, OrderSerializer

class EventAPIView(generics.ListCreateAPIView):
    
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    read_only_fields = ('organizer', 'id')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['event'].queryset = Event.objects.filter(organizer=user)

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class EventAPIRetrieveUpdateDeleteDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TicketAPIView(generics.ListCreateAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    read_only_fields = ('id',)

    def perform_create(self, serialzier):
        serializer.save(organizer=self.request.user)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get the event associated with the ticket
        event = serializer.validated_data['event']

        # Check if the event belongs to the current user
        if event.organizer != request.user:
            return Response({"message": "You can only create tickets for your own events."},
                            status=status.HTTP_403_FORBIDDEN)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TicketAPIRetrieveUpdateDeleteDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_queryset(self):
        user = self.request.user
        events = Event.objects.filter(organizer=user)
        queryset = Ticket.objects.filter(event__in=events)
        return queryset
    

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
    
    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(owner=user)

class OrderAPIRetrieveUpdateDeleteDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

