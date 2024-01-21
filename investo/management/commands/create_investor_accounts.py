# app_name/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from investo.models import InvestorProfile, InvestorAccount
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
                account = InvestorAccount(
                    investor_profile=profile,
                    account_name="TFSA 1",
                    account_id=str(uuid4()),
                    account_type="Investment_Fund_1",
                    status="Open",
                    open_date=datetime.now(),
                    closed_date=None,
                    investment_type="TFSA",
                    add_type="bank_deposit",
                    compound_type="annually"
                )
                account.save()
        self.stdout.write(self.style.SUCCESS('Data seeded successfully.'))
