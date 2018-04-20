from django.contrib import admin
from .models import PatternCategory, PatternTerm

class PatternCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatternCategory, PatternCategoryAdmin)


class PatternTermAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatternTerm, PatternTermAdmin)
