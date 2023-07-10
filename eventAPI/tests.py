from django.test import TestCase
from django.contrib.auth.models import User
from .models import Event, Ticket, Order

import datetime
import pytz

class ModelsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.user = User.objects.create_user(username='test', password='123456', email='test@eventsphere.com')
        cls.purchaser = User.objects.create_user(username="test_2", password="123456", email="test_2@eventsphere.com")

        cls.event = Event.objects.create(
            organizer=cls.user, name='Test Event', 
            start_date=datetime.datetime(2023, 7 , 15, 10, 0, 0, tzinfo=pytz.timezone('Africa/Cairo')),
            end_date=datetime.datetime(2023, 8 , 10, 10, 0, 0, tzinfo=pytz.timezone('Africa/Cairo')), 
            description='test', venue='cairo'
        )

        cls.ticket = Ticket.objects.create(name='test-ticket', description='test', 
        event=cls.event, price=10, available_quantity=10)


        cls.order = Order.objects.create(event=cls.event, owner=cls.purchaser, ticket=cls.ticket, 
        ticket_price=cls.ticket.price, quantity=5, total_price='',)


    
    def test_event_name(self):
        """Test that event name is equal to test"""
        self.assertEqual(self.event.name, 'Test Event')
    
    def test_event_organizer(self):
        """Test event organizer name"""
        self.assertEqual(self.event.organizer.username, 'test')
    
    def test_event_description(self):
        """Test event description"""
        self.assertEqual(self.event.description, 'test')
    
    def test_event_start_date(self):
        """Test event start date and time"""
        expected_date = datetime.datetime(2023, 7 , 15, 10, 0, 0, tzinfo=pytz.timezone('Africa/Cairo'))
        self.assertEqual(self.event.start_date, expected_date)
    
    def test_event_end_date(self):
        """Test event end date and time"""
        expected_date = datetime.datetime(2023, 8 , 10, 10, 0, 0, tzinfo=pytz.timezone('Africa/Cairo'))
        self.assertEqual(self.event.end_date, expected_date)
    
    def test_event_begin_and_end_dates(self):
        """Event's end date must be after start date"""
        start_date = self.event.start_date
        end_date = self.event.end_date
        self.assertGreater(end_date, start_date)
    
    def test_event_venue(self):
        """Test event venue"""
        self.assertEqual(self.event.venue, 'cairo')
    
    def test_ticket_name(self):
        """Test ticket name"""
        self.assertEqual(self.ticket.name, 'test-ticket')
    
    def test_ticket_description(self):
        """Test ticket description"""
        self.assertEqual(self.ticket.description, 'test')
    
    def test_ticket_event_name(self):
        """Test Ticket's event name"""
        self.assertEqual(self.ticket.event.name, self.event.name)
    
    def test_ticket_price(self):
        """Test ticket price"""
        self.assertEqual(self.ticket.price, 10)
    
    def test_ticket_quantity(self):
        """Test ticket available quantity"""
        self.assertEqual(self.ticket.available_quantity, 5) # it will be 5 because of orders down the test file
    
    def test_order_owner(self):
        """Test order's owner"""
        self.assertEqual(self.order.owner.username, self.purchaser.username)
    
    def test_order_event(self):
        """Test order event == event's name"""
        self.assertEqual(self.order.event.name, self.event.name)
    
    def test_order_ticekt_name(self):
        """Test order's ticekt name"""
        self.assertEqual(self.order.ticket.name, self.ticket.name)
    
    def test_order_ticket_price(self):
        """Test order's ticket price"""
        self.assertEqual(self.order.ticket_price, self.ticket.price)
    
    def test_order_ticket_total_price(self):
        """
        Test order's total ticket price = 50, the save() method was called
        """
        self.assertEqual(self.order.total_price, 50)
