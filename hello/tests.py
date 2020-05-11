from django.test import TestCase, Client
from .models import Flight, Airport, Passenger
from django.db.models import Max

class ModelsTestCase(TestCase):

    def setUp(self):

        # Create airports.
        bangkok = Airport.objects.create(code="BKK", city="BANGKOK")
        tokyo = Airport.objects.create(code="HND", city="TOKYO")
        ny = Airport.objects.create(code="JFK", city="NEW YORK")

        # Create flights.
        Flight.objects.create(origin=bangkok, destination=tokyo, duration=5)
        Flight.objects.create(origin=bangkok, destination=bangkok, duration=200)
        Flight.objects.create(origin=bangkok, destination=ny, duration=-100)

    def test_departures_count(self):
        a = Airport.objects.get(code="BKK")
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals_count(self):
        a = Airport.objects.get(code="HND")
        self.assertEqual(a.arrivals.count(), 1)

    def test_valid_flight(self):
        a1 = Airport.objects.get(code="BKK")
        a2 = Airport.objects.get(code="HND")
        f = Flight.objects.get(origin=a1, destination=a2, duration=5)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight_destination(self):
        a1 = Airport.objects.get(code="BKK")
        f = Flight.objects.get(origin=a1, destination=a1)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_duration(self):
        a1 = Airport.objects.get(code="BKK")
        a2 = Airport.objects.get(code="JFK")
        f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
        self.assertFalse(f.is_valid_flight())


class FlightsTestCase(TestCase):


    def setUp(self):

        # Create airports.
        a1 = Airport.objects.create(code="BKK", city="BANGKOK")
        a2 = Airport.objects.create(code="HND", city="TOKYO")
        a3 = Airport.objects.create(code="JFK", city="NEW YORK")

        # Create flights.
        Flight.objects.create(origin=a1, destination=a2, duration=5)
        Flight.objects.create(origin=a1, destination=a3, duration=12)


    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["flights"].count(), 2)

    def test_valid_flight_page(self):
        a1 = Airport.objects.get(code="BKK")
        a2 = Airport.objects.get(code="HND")

        f = Flight.objects.get(origin=a1, destination=a2)

        c = Client()
        response = c.get(f"/{f.id}")
        self.assertEqual(response.status_code, 200)

    def test_invalid_flight_page(self):
        max_id = Flight.objects.all().aggregate(Max("id"))["id__max"]

        c = Client()
        response = c.get(f"/{max_id + 1}")
        self.assertEqual(response.status_code, 404)

    def test_flight_page_passengers(self):
        f = Flight.objects.get(pk=1)
        p = Passenger.objects.create(first="Joe", last="Doe")
        f.passengers.add(p)

        c = Client()
        response = c.get(f"/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["passengers"].count(), 1)

    def test_flight_page_non_passengers(self):
        f = Flight.objects.get(pk=1)
        p = Passenger.objects.create(first="Joe", last="Doe")

        c = Client()
        response = c.get(f"/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["non_passengers"].count(), 1)
