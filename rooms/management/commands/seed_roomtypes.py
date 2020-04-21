from django.core.management import BaseCommand

from rooms.models import RoomType


class Command(BaseCommand):
    help = "Данная команда создает типы жилья"

    def handle(self, *args, **options):
        roomtypes = [
            "Жилье целиком",
            "Отдельная комната",
            "Гостиничный номер",
            "Место в комнате",
        ]

        for rt in roomtypes:
            RoomType.objects.create(name=rt)
        self.stdout.write(self.style.SUCCESS("Типы жилья созданы"))
