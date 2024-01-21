# app_name/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from investo.models import InvestorProfile
from datetime import datetime


class Command(BaseCommand):
    help = 'Seed database with initial user account'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Deleting data...'))
        # Your seeding logic goes here
        InvestorProfile.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Data seeded successfully.'))
