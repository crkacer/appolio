# app_name/management/commands/delete_seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from investo.models import InvestoLicenseType


class Command(BaseCommand):
    help = 'Delete seed data from the database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Deleting seed data...'))
        # Your deletion logic goes here
        InvestoLicenseType.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Seed data deleted successfully.'))
