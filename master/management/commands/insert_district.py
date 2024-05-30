from django.core.management.base import BaseCommand
from master.models import District  # Replace 'myapp' with the name of your Django app

class Command(BaseCommand):
    help = 'Loads Kerala district data into the database'

    def handle(self, *args, **options):
        districts = [
            'Thiruvananthapuram', 'Kollam', 'Pathanamthitta', 'Alappuzha',
            'Kottayam', 'Idukki', 'Ernakulam', 'Thrissur', 'Palakkad',
            'Malappuram', 'Kozhikode', 'Wayanad', 'Kannur', 'Kasaragod'
        ]

        for district in districts:
            District.objects.get_or_create(name=district)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded Kerala districts'))
