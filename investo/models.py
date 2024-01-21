from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from fernet_fields import EncryptedTextField


class InvestorProfile(models.Model):
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
        db_table = 'investor_profile'
        managed = True

    def __str__(self):
        return 'Investor Profile: {} {}'.format(self.first_name, self.last_name)


class InvestorAccount(models.Model):
    investor_profile = models.ForeignKey(InvestorProfile, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_id = models.CharField(max_length=255, blank=True)
    account_type = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, blank=True)
    open_date = models.DateTimeField(max_length=255, blank=True)
    closed_date = models.DateTimeField(max_length=255, blank=True, null=True)
    investment_type = models.CharField(max_length=100, blank=True)
    add_type = models.CharField(max_length=100, blank=True)
    compound_type = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'investor_account'
        managed = True

    def __str__(self):
        return 'Investor Account: {} {} {} {}'.format(
            self.account_name, self.account_type, self.investment_type, self.compound_type
        )


class InvestorAccountTransaction(models.Model):
    account = models.ForeignKey(InvestorAccount, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_name = models.CharField(max_length=255, blank=True)
    transaction_type = models.CharField(max_length=20, blank=True)
    amount = models.IntegerField(default=0)
    datetime = models.DateTimeField(max_length=255, blank=True)

    class Meta:
        db_table = 'investor_account_transaction'
        managed = True

    def __str__(self):
        return 'Investor Account Transaction: {} {} {} {}'.format(
            self.transaction_name, self.transaction_type, self.amount, self.datetime
        )


class InvestorAccountTransfer(models.Model):
    account = models.ForeignKey(InvestorAccount, on_delete=models.CASCADE)
    transfer_bank = EncryptedTextField()
    transfer_account_number = EncryptedTextField()
    transfer_type = EncryptedTextField()
    transfer_amount = EncryptedTextField()

    class Meta:
        db_table = "investor_account_transfer"
        managed = True


class InvestorAccountDeposit(models.Model):
    account = models.ForeignKey(InvestorAccount, on_delete=models.CASCADE)
    account_institution_number = EncryptedTextField()
    account_institution_name = EncryptedTextField()
    account_transit_number = EncryptedTextField()
    account_account_number = EncryptedTextField()
    account_deposit_amount = EncryptedTextField()

    class Meta:
        db_table = "investor_account_deposit"
        managed = True


class InvestorAccountMeta(models.Model):
    account = models.ForeignKey(InvestorAccount, on_delete=models.CASCADE)
    meta_name = models.CharField(max_length=255, blank=False)
    meta_value = models.CharField(max_length=255, blank=False)

    class Meta:
        db_table = "investor_account_meta"
