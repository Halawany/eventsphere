from django.urls import path, include

from .views import (
    EventAPIView, 
    EventAPIRetrieveUpdateDeleteDestroy as EventAPIOps,
    TicketAPIView,
    TicketAPIRetrieveUpdateDeleteDestroy as TicketAPIOps,
    OrderAPIView,
    OrderAPIRetrieveUpdateDeleteDestroy as OrderOps
)

urlpatterns = [
    path('api/', EventAPIView.as_view(), name='event_apiview'),
    path('api/event/<int:pk>', EventAPIOps.as_view(), name="event_op"),
    path('api/tickets/', TicketAPIView.as_view(), name='ticket_apiview'),
    path('api/tickets/<int:pk>', TicketAPIOps.as_view(), name='ticket_op'),
    path('api/orders/', OrderAPIView.as_view(), name='order_apiview'),
    path('api/orders/<int:pk>', OrderOps.as_view(), name='order_op'),

]
