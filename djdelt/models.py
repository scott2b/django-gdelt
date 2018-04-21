from django.db import models


class PatternCategory(models.Model):
    name = models.CharField(max_length=35)
    cat_type = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'pattern categories'

    def __str__(self):
        return '%s (%s)' % (self.name, self.cat_type)


class PatternTerm(models.Model):
    category = models.ForeignKey(PatternCategory, on_delete=models.CASCADE)
    term = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return '%s (%s)' % (self.term, self.category.name)


class GKGDocument(models.Model):
    WEB = 1
    CITATIONONLY = 2
    CORE = 3
    DTIC = 4
    JSTOR = 5
    NONTEXTUALSOURCE = 6
    SOURCE_COLLECTION_CHOICES = (
        (WEB, 'Web'),
        (CITATIONONLY, 'Citation only'),
        (CORE, 'Core'),
        (DTIC, 'DTIC'),
        (JSTOR, 'JSTOR'),
        (NONTEXTUALSOURCE, 'Non-textual'),
    )
    gkg_record_id = models.CharField(max_length=20, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    source_collection = models.IntegerField(choices=SOURCE_COLLECTION_CHOICES)
    source_common_name = models.CharField(max_length=100)
    document_identifier = models.CharField(max_length=1024)
    v1counts = models.TextField(blank=True)
    v2counts = models.TextField(blank=True)
    v1themes = models.TextField(blank=True)
    v2themes = models.TextField(blank=True)
    v1locations = models.TextField(blank=True)
    v2locations = models.TextField(blank=True)
    v1persons = models.TextField(blank=True)
    v2persons = models.TextField(blank=True)
    v1organizations = models.TextField(blank=True)
    v2organizations = models.TextField(blank=True)
    tone = models.TextField(blank=True)
    dates = models.TextField(blank=True)
    gcam = models.TextField(blank=True)
    sharing_image = models.URLField(blank=True)
    quotations = models.TextField(blank=True)
    all_names = models.TextField(blank=True)
    amounts = models.TextField(blank=True)
    translation_info = models.TextField(blank=True)
    extras_xml = models.TextField(blank=True)

    def __str__(self):
        return '%s: %s' % (self.gkg_record_id, self.document_identifier)


class GKGMedia(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('RELATED_IMAGE', 'Related image'),
        ('SOCIAL_IMAGE_EMBED', 'Social image embed'),
        ('SOCIAL_VIDEO_EMBED', 'Social video embed'),
    )
    document = models.ForeignKey(GKGDocument, on_delete=models.CASCADE)
    url = models.URLField()
    media_type = models.CharField(max_length=18)
    media_type = models.CharField(max_length=18)


class Classifier(object):

    @classmethod
    def classify_text(cls, text):
        text = text.lower()
        info = {}
        for term in PatternTerm.objects.all():
            if term.term in text:
                cat = term.category
                cat_name = term.category.name
                cat_type = term.category.cat_type
                if not cat_type in info:
                    info[cat_type] = {}
                if not cat_name in info[cat_type]:
                    info[cat_type][cat_name] = 0
                info[cat_type][cat_name] += term.score
        for type_, categories in info.items():
            collection = { cat:score for cat, score in categories.items() if score > 0 }
            if collection:
                info[type_] = collection
            else:
                del(info[type_])
        return info
