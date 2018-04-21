"""
The patterns file is here: https://github.com/ahalterman/GKG-Themes/blob/master/SET_EVENTPATTERNS.xml
A local copy is kept in resources

It is not valid XML so we use regex

There are non-theme entries in this file not considered here
"""
import re
from urllib import request
from django.core.management.base import BaseCommand, CommandError
from djdelt.models import PatternCategory, PatternTerm

SET_EVENTPATTERNS_URL = 'https://raw.githubusercontent.com/ahalterman/GKG-Themes/master/SET_EVENTPATTERNS.xml'

globals_p = re.compile(r'^<GLOBAL>\s*<TERMS>([^<]+)</TERMS>', re.M|re.S)
categories_p = re.compile(r'^<CATEGORY NAME="([^"]+)" TYPE="([^"]+)">\s*<TERMS>([^<]+)</TERMS>', re.M|re.S)


class Command(BaseCommand):
    help = 'Load publicly available Gdelt patterns into the system'

    def handle(self, *args, **options):
        doc = request.urlopen(SET_EVENTPATTERNS_URL).read().decode('utf-8')
        global_terms = []
        categories = {}
        for text in globals_p.findall(doc):
            for line in text.split('\n'):
                ts = line.split('\t')
                if len(ts) == 2:
                    global_terms.append( (ts[0], int(ts[1])) )
        for cat, type_, terms in categories_p.findall(doc):
            cat_obj, created = PatternCategory.objects.get_or_create(
                name=cat, cat_type=type_)
            for term, score in [(t.split('\t')[0], int(t.split('\t')[1])) for t in
                    terms.split('\n') if t and len(t.split('\t')) == 2]:
                term_obj = PatternTerm.objects.get_or_create(
                    category=cat_obj, term=term, score=score)
