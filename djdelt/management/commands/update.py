import csv
from io import BytesIO, StringIO, TextIOWrapper
import zipfile
import re
from django.core.management.base import BaseCommand, CommandError
from urllib import request

LAST_UPDATE_URL = 'http://data.gdeltproject.org/gdeltv2/lastupdate.txt'
GKG_RE = re.compile(b'http://.*?.gkg.csv.zip')

class Command(BaseCommand):
    help = 'Update gkg to the last 15 minute update'

    def handle(self, *args, **options):
        txt = request.urlopen(LAST_UPDATE_URL).read()
        url = GKG_RE.search(txt).group().decode('utf-8')
        with zipfile.ZipFile(BytesIO(request.urlopen(url).read())) as zf:
            #assert len == 1 and .gkg.csv
            f = zf.namelist()[0]
            with zf.open(f, 'r') as csvfile:
                reader = csv.reader(TextIOWrapper(csvfile), delimiter='\t')
                for row in reader:
                    (GKGRECORDID, V21DATE, V2SOURCECOLLECTIONIDENTIFIER, \
                    V2SOURCECOMMONNAME, V2DOCUMENTIDENTIFIER, \
                    V1COUNTS, V21COUNTS, V1THEMES, V2ENHANCEDTHEMES, \
                    V1LOCATIONS, V2ENHANCEDLOCATIONS, V1PERSONS,
                    V2ENHANCEDPERSONS, V1ORGANIZATIONS,
                    V2ENHANCEDORGANIZATIONS, V15TONE,
                    V21ENHANCEDDATES, V2GCAM, V21SHARINGIMAGE,
                    V21RELATEDIMAGES, V21SOCIALIMAGEEMBEDS,
                    V21SOCIALVIDEOEMBEDS, V21QUOTATIONS,
                    V21ALLNAMES, V21AMOUNTS, V21TRANSLATIONINFO,
                    V2EXTRASXML) = tuple(row)
                    print(V21AMOUNTS)

