from django.contrib import admin
from .models import PatternCategory, PatternTerm, GKGDocument, GKGMedia

class PatternCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatternCategory, PatternCategoryAdmin)


class PatternTermAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatternTerm, PatternTermAdmin)


class GKGMediaInline(admin.TabularInline):
    model = GKGMedia
    extra = 0


class GKGDocumentAdmin(admin.ModelAdmin):
    pass
    inlines = (
        GKGMediaInline,
    )
admin.site.register(GKGDocument, GKGDocumentAdmin)
