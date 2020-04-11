import random

from django.core.management import BaseCommand
from django_seed import Seed

from reviews.models import Review
from rooms.models import Room
from users.models import User


class Command(BaseCommand):
    help = 'Generate fake reviews for rooms'

    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int, help='Type number of reviews')

    def handle(self, *args, **options):
        number = options.get('number')  # получаем дополнительный параметр

        users = User.objects.all()  # получаем всех пользователей
        rooms = Room.objects.all()  # получаем все комнаты

        seeder = Seed.seeder()  # инициализируем сидер для генерации данных
        seeder.add_entity(Review, number, {
            'accuracy': lambda x: random.randint(1, 5),
            'communication': lambda x: random.randint(1, 5),
            'cleanliness': lambda x: random.randint(1, 5),
            'location': lambda x: random.randint(1, 5),
            'check_in': lambda x: random.randint(1, 5),
            'value': lambda x: random.randint(1, 5),
            'user': lambda x: random.choice(users),
            'room': lambda x: random.choice(rooms),
        })
        seeder.execute()  # Запускаем на выполнение
        self.stdout.write(self.style.SUCCESS(f'created {number} reviews'))
