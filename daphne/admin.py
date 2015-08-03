from django.contrib import admin
from daphne import models as m

admin.site.register(m.Page)
admin.site.register(m.Section)
admin.site.register(m.TextImageSection)
admin.site.register(m.GallerySection)
admin.site.register(m.Template)
