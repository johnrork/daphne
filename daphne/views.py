from daphne import models as m
from django.shortcuts import render, get_object_or_404
from django.template.loader import select_template
from collections import defaultdict

def test(request, **kwargs):
    content = []
    page = get_object_or_404(m.Page, slug=kwargs.get('slug'))
    sections = page.section_set.order_by('type')
    order = {s.ident(): s.order for s in sections }
    classes = {s.ident(): s.classes for s in sections}
    lookups = defaultdict(list)
    for section in sections:
        lookups[section.type].append(section.related_id)
    for key, pk_list in lookups.iteritems():
        model = getattr(m, key)
        content.extend(model.objects.filter(id__in=pk_list))
    page.content = sorted(content, key=lambda x: order[x.ident()])
    for c in page.content:
        c.classes = classes[c.ident()]
    page.data = {m.ident(): m for m in content}
    return render(request, [page.template.file, 'default.html'], {'page':page})

def react_playground(request, **kwargs):
    return render(request, 'react_playground.html')

def home(request):
    pass
