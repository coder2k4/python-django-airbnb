import random

from django.contrib.admin.utils import flatten
from django.core.management import BaseCommand
from django_seed import Seed

from lists.models import List
from rooms.models import Room
from users.models import User


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            type=int,
            default=1,
            help='Generate NUMBER of lists'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        rooms = Room.objects.all()
        users = User.objects.all()
        seeder.add_entity(List, number, {
            'user': lambda x: random.choice(users)
        })
        created_list_ids = seeder.execute()
        cls_list_ids = flatten(list(created_list_ids.values()))
        for pk in cls_list_ids:
            list_model = List.objects.get(pk=pk)
            to_add = rooms[random.randint(0, 5): random.randint(6, 30)]
            list_model.rooms.add(*to_add)  # звездочка получает доступ только к значениям массива
        self.stdout.write(self.style.SUCCESS(f'{number} листов было добавлено'))
