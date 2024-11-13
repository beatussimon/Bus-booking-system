from django.db import models

# Create your models here.

class Bus_stand(models.Model):
    location_name = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.location_name}"

class Passenger(models.Model):
    first_name =models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name  }"

class Buses(models.Model):
    origin = models.ForeignKey(Bus_stand, on_delete=models.CASCADE, related_name="departures")
    destination= models.ForeignKey(Bus_stand, on_delete=models.CASCADE, related_name="arrivals")
    duration= models.IntegerField(null=False)
    passenger = models.ManyToManyField(Passenger, related_name="onboard")

    def __str__(self):
        return f"from {self.origin} to {self.destination} - {self.duration}"
