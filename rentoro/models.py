from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class LandlordProfile(models.Model):
    email = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    dob = models.CharField(max_length=255, blank=True)
    SIN = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.IntegerField(default=0)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'landlord_profile'
        managed = True

    def __str__(self):
        return 'Landlord Profile: {} {}'.format(self.first_name, self.last_name)


class TenantProfile(models.Model):
    email = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    dob = models.CharField(max_length=255, blank=True)
    SIN = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.IntegerField(default=0)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'tenant_profile'
        managed = True

    def __str__(self):
        return 'Tenant Profile: {} {}'.format(self.first_name, self.last_name)


class RentalProperty(models.Model):
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=255, blank=True)
    bedrooms = models.FloatField(default=0)
    washrooms = models.FloatField(default=0)
    parking = models.IntegerField(default=0)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.IntegerField(default=0)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'rental_property'
        managed = True

    def __str__(self):
        return 'Rental Property: {} Owner ID: {}'.format(self.name, self.landlord)


class RentalPropertyPhoto(models.Model):
    file_location = models.CharField(max_length=255, blank=True)
    property = models.ForeignKey(RentalProperty, on_delete=models.CASCADE)

    class Meta:
        db_table = 'rental_property_photo'
        managed = True

class LeasingProperty(models.Model):

    pass


