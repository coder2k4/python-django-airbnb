import random

from django.contrib.admin.utils import flatten
from django.core.management import BaseCommand
from django_seed import Seed

from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = 'This command create many rooms'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            default=1,
            type=int,
            help=(
                'This command create NUMBER rooms'
            ),
        )

    def handle(self, *args, **options):
        # получаем из командной строки количество пользователей, по дефолту 1
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.company(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_IDs = seeder.execute()
        cln_created_IDs = flatten(list(created_IDs.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in cln_created_IDs:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f'/room_photos/{random.randint(1, 31)}.webp'
                )
            for a in amenities:
                if random.randint(0, 1) == 0:
                    room.amenity.add(a)

            for f in facilities:
                if random.randint(0, 1) == 0:
                    room.facility.add(f)

            for r in rules:
                if random.randint(0, 1) == 0:
                    room.house_rules.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
