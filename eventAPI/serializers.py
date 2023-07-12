from rest_framework import serializers

from .models import Event, Ticket, Order

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'organizer', 'name', 'start_date', 'end_date', 'description', 'venue')
        read_only_fields = ('id', 'organizer', )

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('id', 'event', 'name', 'description', 'price', 'available_quantity')
        read_only_fields = ('id',)

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'owner', 'ticket', 'event', 'ticket_price', 'quantity', 'total_price')
        read_only_fields = ('id', 'owner', 'event', 'ticket_price', 'total_price')