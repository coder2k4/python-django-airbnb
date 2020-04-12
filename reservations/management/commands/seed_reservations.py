import random

from django.core.management import BaseCommand
from django_seed import Seed
from datetime import datetime, timedelta

from reservations.models import Reservation
from rooms.models import Room
from users.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--number',
                            type=int,
                            default=1,
                            help='Create NUMBER of reservations')

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        users = User.objects.all()
        rooms = Room.objects.all()
        seeder.add_entity(Reservation, number, {
            'room': lambda x: random.choice(rooms),
            'guest': lambda x: random.choice(users),
            'check_in': lambda x: datetime.now(),
            'check_out': lambda x: datetime.now() + timedelta(days=random.randint(3, 25))
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} reservations successfully created '))
