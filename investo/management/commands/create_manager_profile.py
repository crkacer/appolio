# app_name/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from investo.models import ManagerProfile
from datetime import datetime


class Command(BaseCommand):
    help = 'Seed database with initial user account'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))
        # Your seeding logic goes here
        user = User.objects.filter(email="test.manager@appolio.ca").first()
        if user:
            profile = ManagerProfile(
                email="test.manager@appolio.ca",
                first_name="Test",
                last_name="Manager",
                middle_name="",
                dob="01-01-1990",
                SIN="000000000",
                address="123 Abc St.",
                city="Toronto",
                province="ON",
                postal_code="M1G 2B3",
                phone="416-999-0000",
                status="Open",
                user=user,
                completed=1,
                updated_at=datetime.now(),
                created_at=datetime.now()
            )
            profile.save()
        self.stdout.write(self.style.SUCCESS('Data seeded successfully.'))
