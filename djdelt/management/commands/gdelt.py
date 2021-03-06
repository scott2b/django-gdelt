import datetime
import json
import gdelt
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import DataError
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
            doc = GKGDocument.objects.filter(gkg_record_id=item['GKGRECORDID']).first()
            if doc:
                print('Skipping existing: %s' % item['GKGRECORDID'])
            else:
                print(item['GKGRECORDID'])
                doc = GKGDocument()
                doc.gkg_record_id = item['GKGRECORDID']
                try:
                    dt = datetime.datetime.strptime(str(item['DATE']), '%Y%m%d%H%M%S')
                except ValueError:
                    dt = None
                doc.date = dt
                doc.source_collection = item['SourceCollectionIdentifier']
                doc.source_common_name = item['SourceCommonName'] or ''
                doc.document_identifier = item['DocumentIdentifier'] or ''
                doc.v1counts = item['Counts'] or ''
                doc.v2counts = item['V2Counts'] or ''
                doc.v1themes = item['Themes'] or ''
                doc.v2themes = item['V2Themes'] or ''
                doc.v1locations = item['Locations'] or ''
                doc.v2locations = item['V2Locations'] or ''
                doc.v1persons = item['Persons'] or ''
                doc.v2persons = item['V2Persons'] or ''
                doc.v1organizations = item['Organizations'] or ''
                doc.v2organizations = item['V2Organizations'] or ''
                doc.tone = item['V2Tone'] or ''
                doc.dates = item['Dates'] or ''
                doc.gcam = item['GCAM'] or ''
                img = item['SharingImage'] or ''
                doc.sharing_image = img[:1024]
                doc.quotations = item['Quotations'] or ''
                doc.all_names = item['AllNames'] or ''
                doc.amounts = item['Amounts'] or ''
                doc.translation_info = item['TranslationInfo'] or ''
                doc.extras_xml = item['Extras'] or ''
                try:
                    doc.save()
                except DataError:
                    print('Unable to save GKG Document: %s' % doc.gkg_record_id)
                    continue
                for url in item['RelatedImages'].split(';') \
                        if item['RelatedImages'] else []:
                    if url.strip():
                        GKGMedia(
                            document=doc,
                            url=url.strip()[:1024],
                            media_type='RELATED_IMAGE').save()
                for url in item['SocialImageEmbeds'].split(';') \
                        if item['SocialImageEmbeds'] else []:
                    if url.strip():
                        GKGMedia(
                            document=doc,
                            url=url.strip()[:1024],
                            media_type='SOCIAL_IMAGE_EMBED').save()
                for url in item['SocialVideoEmbeds'].split(';') \
                        if item['SocialVideoEmbeds'] else []:
                    if url.strip():
                        GKGMedia(
                            document=doc,
                            url=url.strip()[:1024],
                            media_type='SOCIAL_VIDEO_EMBED').save()
