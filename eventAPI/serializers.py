from rest_framework import serializers

from .models import Event, Ticket, Order

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'organizer', 'name', 'start_date', 'end_date', 'description', 'venue')
        read_only_fields = ('id', 'organizer', )

class TicketSerializer(serializers.ModelSerializer):
    event = serializers.HyperlinkedRelatedField(view_name='event_detail', queryset=Event.objects.none())
    event_details = EventSerializer(source='event', read_only=True)

    class Meta:
        model = Ticket
        fields = ('id', 'event', 'organizer', 'event_details',  'name', 'description', 'price', 'available_quantity')
        read_only_fields = ('id', 'organizer')
    
    def get_event(self, obj):
        print("get_event method called")
        request = self.context.get('request')
        queryset = Event.objects.filter(organizer=request.user)
        serializer = EventSerializer(queryset, many=True, context={'request': request})
        return serializer.data

class OrderSerializer(serializers.ModelSerializer):

    ticket_string = serializers.StringRelatedField()
    ticket_details = TicketSerializer(source='ticket', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'owner', 'ticket', 'ticket_string', 'ticket_details', 'event', 'ticket_price', 'quantity', 'total_price')
        read_only_fields = ('id', 'owner', 'event', 'ticket_price', 'total_price')