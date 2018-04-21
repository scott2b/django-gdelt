from djdelt.models import PatternTerm


def classify_text(text):
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
