# app_name/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Seed database with initial user account'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))
        # Your seeding logic goes here
        User.objects.create_user(
            username="test.user",
            email="test.user@appolio.ca",
            password="testing123"
        )
        self.stdout.write(self.style.SUCCESS('Data seeded successfully.'))
