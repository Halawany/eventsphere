from django.urls import path, include

from .views import EventAPIView, EventAPIRetrieveUpdateDeleteDestroy as _

urlpatterns = [
    path('api/', EventAPIView.as_view(), name='event_apiview'),
    path('api/event/<int:pk>', _.as_view(), name="event-op"),
]
