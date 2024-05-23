from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=100)
    country_name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=10, decimal_places=5)
    latitude = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return f"{self.city_name}, {self.country_name}"
