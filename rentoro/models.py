from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

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


class RentalPropertyType(models.Model):
    type_name = models.CharField(max_length=255, blank=True)
    type_slug = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'rental_property_type'
        managed = True


class RentalProperty(models.Model):
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=255, blank=True)
    rental_id = models.CharField(max_length=255, blank=True)
    property_type = models.ForeignKey(RentalPropertyType, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, blank=True)
    owner = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'rental_property'
        managed = True

    def __str__(self):
        return 'Rental Property: {} {}'.format(self.address, self.city)


class RentalPropertyUnit(models.Model):
    unit_name = models.CharField(max_length=255, blank=True)
    unit_id = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=255, blank=True)
    property = models.ForeignKey(RentalProperty, on_delete=models.CASCADE)
    tenant = models.ManyToManyField(TenantProfile)
    status = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'rental_property_unit'
        managed = True

    def __str__(self):
        return 'Rental Property Unit: {} {}'.format(self.unit_name, self.address)


class RentalPropertyTransactionType(models.Model):
    transaction_name = models.CharField(max_length=255, blank=True)
    transaction_slug = models.CharField(max_length=255, blank=True)
    transaction_type = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'rental_property_transaction_type'
        managed = True


class RentalPropertyTransaction(models.Model):
    transaction_name = models.CharField(max_length=255, blank=True)
    transaction_id = models.CharField(max_length=255, blank=True)
    property_unit = models.ForeignKey(RentalPropertyUnit, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(RentalPropertyTransactionType, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'rental_property_transaction'
        managed = True
