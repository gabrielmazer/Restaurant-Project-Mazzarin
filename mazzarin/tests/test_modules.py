from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : $80")
        
class BookingTest(TestCase):
    
    def test_get_item(self):
        item = Booking.objects.create(first_name="Boby Tester", reservation_date="2023-11-25", no_of_guests="5")
        self.assertEqual(str(item), "Boby Tester : 2023-11-25 : 5 guests")