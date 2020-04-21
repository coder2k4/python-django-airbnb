from django.core.management import BaseCommand

from rooms.models import HouseRule


class Command(BaseCommand):
    help = "Данная команда создает правила пользования жильем"

    def handle(self, *args, **options):
        houserules = [
            "Не курить",
            "Держать все в чистоте",
            "Без животных",
            "Без вечеринок",
            "Без гостей",
            "Без алкоголя",
        ]

        for hr in houserules:
            HouseRule.objects.create(name=hr)
        self.stdout.write(self.style.SUCCESS("Типы жилья созданы"))
