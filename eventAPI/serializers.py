from rest_framework import serializers

from .models import Event, Ticket, Order

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'organizer', 'name', 'start_date', 'end_date', 'description', 'venue')
        read_only_fields = ('id', 'organizer', )

class TicketSerializer(serializers.ModelSerializer):

    # event = serializers.HyperlinkedRelatedField(view_name='event_list', read_only=True, lookup_field='id', queryset=Event.objects.all())
    event_details = EventSerializer(source='event', read_only=True)

    class Meta:
        model = Ticket
        fields = ('id', 'event', 'event_details',  'name', 'description', 'price', 'available_quantity')
        read_only_fields = ('id', )

class OrderSerializer(serializers.ModelSerializer):

    ticket_string = serializers.StringRelatedField()
    ticket_details = TicketSerializer(source='ticket', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'owner', 'ticket', 'ticket_string', 'ticket_details', 'event', 'ticket_price', 'quantity', 'total_price')
        read_only_fields = ('id', 'owner', 'event', 'ticket_price', 'total_price')