import json
import gdelt
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone


class Command(BaseCommand):
    help = 'Get updates from GDELT'

    def add_arguments(self, parser):
        parser.add_argument('table', nargs=1, type=str, choices=('events', 'mentions', 'gkg') )
        parser.add_argument('dates', nargs='?', type=str)
        parser.add_argument(
            '--coverage',
            action='store_true',
            dest='coverage',
            help='Fetch full coverage in specified date range'
        )

    def handle(self, table, dates, *args, **options):
        table = table[0]
        if not dates:
            dates = timezone.now().date().isoformat()
        gd2 = gdelt.gdelt(version=2)
        coverage = options['coverage']
        results = gd2.Search(dates, table=table, output='json', coverage=coverage)
        j = json.loads(results)
        for k,v in j[0].items():
            print('%s: %s' % (k,v))

