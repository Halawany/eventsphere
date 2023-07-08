from django.contrib import admin

from .models import Event, Ticket, Order

admin.site.register(Event)
admin.site.register(Ticket)

class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('ticket_price', 'total_price')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('ticket', 'event', 'quantity')
        else:
            return self.readonly_fields

admin.site.register(Order, OrderAdmin)
