import datetime
import json
import gdelt
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from djdelt.models import GKGDocument, GKGMedia


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
        data = json.loads(results)
        for item in data:
            print(item)
            for k,v in item.items():
                print('%s: %s' % (k, v))
            try:
                doc = GKGDocument.objects.get(gkg_record_id=item['GKGRECORDID'])
            except GKGDocument.DoesNotExist:
                doc = GKGDocument()
                doc.gkg_record_id = item['GKGRECORDID']
                dt = datetime.datetime.strptime(str(item['DATE']), '%Y%m%d%H%M%S')
                doc.date = dt
                doc.source_collection = item['SourceCollectionIdentifier']
                doc.source_common_name = item['SourceCommonName']
                doc.document_identifier = item['DocumentIdentifier']
                doc.v1counts = item['Counts'] or ''
                doc.v2counts = item['V2Counts'] or ''
                doc.v1themes = item['Themes'] or ''
                doc.v2themes = item['V2Themes'] or ''
                doc.v1locations = item['Locations'] or ''
                doc.v2locations = item['Persons'] or ''
                doc.v1persons = item['Persons'] or ''
                doc.v2persons = item['V2Persons'] or ''
                doc.v1organizations = item['Organizations'] or ''
                doc.v2organizations = item['V2Organizations'] or ''
                doc.tone = item['V2Tone'] or ''
                doc.dates = item['Dates'] or ''
                doc.gcam = item['GCAM'] or ''
                doc.sharing_image = item['SharingImage'] or ''
                doc.quotations = item['Quotations'] or ''
                doc.all_names = item['AllNames'] or ''
                doc.amounts = item['Amounts'] or ''
                doc.translation_info = item['TranslationInfo'] or ''
                doc.extras_xml = item['Extras'] or ''
                doc.save()
                for url in item['RelatedImages'].split(';') \
                        if item['RelatedImages'] else []:
                    if url.strip():
                        GKGMedia(
                            document=doc,
                            url=url.strip(),
                            media_type='RELATED_IMAGE').save()
                for url in item['SocialImageEmbeds'].split(';') \
                        if item['SocialImageEmbeds'] else []:
                    if url.strip():
                        GKGMedia(
                            document=doc,
                            url=url.strip(),
                            media_type='SOCIAL_IMAGE_EMBED').save()
                for url in item['SocialVideoEmbeds'].split(';') \
                        if item['SocialVideoEmbeds'] else []:
                    if url.strip():
                        GKGMedia(
                            document=doc,
                            url=url.strip(),
                            media_type='SOCIAL_VIDEO_EMBED').save()
