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
