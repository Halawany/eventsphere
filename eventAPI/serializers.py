from rest_framework import serializers

from .models import Event, Ticket, Order

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'organizer', 'name', 'start_date', 'end_date', 'description', 'venue')
        read_only_fields = ('id', 'organizer', )
