# app_name/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from investo.models import InvestoLicenseType, InvestoLicense, ManagerProfile

class Command(BaseCommand):
    help = 'Seed database with initial user account'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))
        # Your seeding logic goes here
        new_license_1 = InvestoLicenseType(license_type="STARTER")
        new_license_1.save()
        new_license_2 = InvestoLicenseType(license_type="PREMIUM")
        new_license_2.save()
        new_license_3 = InvestoLicenseType(license_type="EXTENDED")
        new_license_3.save()

        self.stdout.write(self.style.SUCCESS('Data seeded successfully.'))
