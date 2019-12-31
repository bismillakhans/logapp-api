from django.db import models

vtypes = (
    ('two_wheeler', "Two Wheeler"),
    ('three_wheeler', "Three Wheeler"),
    ('four_wheeler', "Four Wheeler"),
    ('heavy', "Heavy Vehicle"),
)


# Create your models here.
class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=120)
    vehicle_type = models.CharField(max_length=120, choices=vtypes, default=vtypes[0][0])
    mobile_number = models.CharField(max_length=120, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.vehicle_number


class Entry(models.Model):
    vehicle_number = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    time_arrival = models.DateTimeField(auto_now_add=True)
    time_leave = models.DateTimeField(null=True, blank=True)
    time_duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.vehicle_number
