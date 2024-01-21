# app_name/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from investo.models import InvestorProfile, InvestorAccount, InvestorAccountTransaction
from datetime import datetime, date
from uuid import uuid4

class Command(BaseCommand):
    help = 'Seed database with initial user account'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))
        # Your seeding logic goes here
        user = User.objects.filter(username="test.user").first()
        if user:
            profile = InvestorProfile.objects.filter(user=user).first()
            if profile:
                account = InvestorAccount.objects.filter(account_name="TFSA 1").first()
                if account:
                    account_transaction = InvestorAccountTransaction(
                        account=account,
                        transaction_id=str(uuid4()),
                        transaction_name="Initial Investment",
                        transaction_type="Investor_Deposit",
                        amount=100000,
                        datetime=datetime.now()
                    )
                    account_transaction.save()
        self.stdout.write(self.style.SUCCESS('Data seeded successfully.'))
