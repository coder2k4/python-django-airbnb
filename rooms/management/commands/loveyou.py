from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Just test how much i love you.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--times',
            help=(
                'Just test how much TIMES i love you.'
            ),
        )

    def handle(self, *args, **options):
        print(self, args, options)
        times = options.get('times')
        for time in range(0, int(times)):
            self.stdout.write(self.style.ERROR("I love you"))
            print('I LOVE YOU')
