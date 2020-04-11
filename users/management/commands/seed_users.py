from django.core.management import BaseCommand
from django_seed import Seed

from users.models import User


class Command(BaseCommand):
    help = 'This command create many users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            default=1,
            help=(
                'This command create NUMBER users'
            ),
        )

    def handle(self, *args, **options):
        # получаем из командной строки количество пользователей, по дефолту 1
        numberToCreate = int(options.get('number'))
        seeder = Seed.seeder()
        seeder.add_entity(User, numberToCreate, {
            'is_staff': False,
            'is_superuser': False,
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{numberToCreate} users created!'))
