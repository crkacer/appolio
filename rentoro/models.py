from django.db import models
from django.contrib.auth.models import User,  AbstractUser, Group, Permission
from datetime import datetime

# Create your models here.


class User(AbstractUser):
    # Add any additional fields you want in your custom user model
    # For example:
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
    
    email = models.CharField(max_length=250, unique=True, null=False, blank=False)
    REGISTRATION_CHOICES = [
        ('email', 'Email'),
        ('google', 'Google'),
    ]
    registration_method = models.CharField(
        max_length=10,
        choices=REGISTRATION_CHOICES,
        default='email'
    )

    def __str__(self):
       return self.username
    

class UserVerification(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verify_code = models.CharField(max_length=6, blank=True)
    expiry_date = models.DateTimeField(blank=True)
    status = models.CharField(max_length=50, blank=True)

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



class RentalPropertyShare(models.Model):

    rental = models.ForeignKey(RentalProperty, on_delete=models.CASCADE)
    unique_code = models.CharField(max_length=100, blank=True)
    expire_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

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


class RentalApplicationOtherTransaction(models.Model):
    application = models.ForeignKey('RentalApplication', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=255, blank=True)
    transaction_due_date = models.DateTimeField(default=datetime.now, blank=True)
    transaction_amount = models.FloatField(default=0)


    class Meta:
        db_table = 'rental_application_other_transaction'
        managed = True


class RentalApplicationFee(models.Model):
    application = models.ForeignKey('RentalApplication', on_delete=models.CASCADE)
    fee_type = models.CharField(max_length=255, blank=True)
    fee_amount_type = models.CharField(max_length=255, blank=True) # fixed or percentage
    fee_due_date = models.DateTimeField(default=datetime.now, blank=True)
    fee_amount = models.FloatField(default=0)

    class Meta:
        db_table = 'rental_application_fee'
        managed = True


class RentalApplicationUtility(models.Model):
    application = models.ForeignKey('RentalApplication', on_delete=models.CASCADE)
    utility_name = models.CharField(max_length=255, blank=True)
    utility_owner = models.CharField(max_length=255, blank=True) # landlord or tenant or N/A

    class Meta:
        db_table = 'rental_application_utility'
        managed = True


class RentalApplicationInsurance(models.Model):
    application = models.ForeignKey('RentalApplication', on_delete=models.CASCADE)
    insurance_name = models.CharField(max_length=255, blank=True)
    # TODO: Insurance Details
    # 

    class Meta:
        db_table = 'rental_application_insurance'
        managed = True


class RentalApplication(models.Model):
    application_id = models.CharField(max_length=255, blank=True)
    property_unit = models.ForeignKey(RentalPropertyUnit, on_delete=models.CASCADE)
    tenant = models.ForeignKey(TenantProfile, on_delete=models.CASCADE)
    # Tenant Application's details
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    dob = models.CharField(max_length=255, blank=True)
    SIN = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)

    # Rental Application's details
    rental_type = models.CharField(max_length=255, blank=True)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(default=datetime.now, blank=True)

    # Payment Details
    payment_schedule_type = models.CharField(max_length=255, blank=True)
    payment_start_date = models.DateTimeField(default=datetime.now, blank=True)
    payment_amount = models.FloatField(default=0)

    deposit_amount = models.FloatField(default=0)


    status = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'rental_application'
        managed = True

    def __str__(self):
        return 'Rental Application: {}'.format(self.application_id)