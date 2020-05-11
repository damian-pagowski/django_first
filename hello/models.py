from django.db import models
from django.core.exceptions import ValidationError


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}"
    
    def is_valid_flight(self):
      return (self.origin != self.destination) and (self.duration >= 0)


    # def clean(self):
    #     if self.origin == self.destination:
    #         raise ValidationError("Origin and destination must be different.")
    #     elif self.duration < 1:
    #         raise ValidationError("Duration must be positive.")

    # # Call this method before trying to add data, overriding the default behavior of built-in `save`.
    # def save(self, *args, **kwargs):
    #     self.clean()

    #     # This syntax now calls Django's own "save" function, adding this data to the DB (if `clean` was ok).
    #     super().save(*args, **kwargs)

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"


