from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from .validators import AllowPositiveDecimalValuesOnly

class Event(models.Model):

    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=1000, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=False, blank=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=False, blank=False)
    venue = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):

        return f"{self.name} organized by {self.organizer}"
    
class Ticket(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=False, blank=False, 
    validators=[AllowPositiveDecimalValuesOnly,])
    available_quantity = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):

        return f"{self.name} Ticket from Event {self.event}"

class Order(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='orders', 
    null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='orders')
    ticket_price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=15, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.ticket:
            self.ticket_price = self.ticket.price
            self.total_price = self.ticket_price * self.quantity
        super(Order, self).save(*args, **kwargs)

    def __str__(self):

        return f"Order of {self.quantity} Tickets by {self.owner} From event {self.event}"