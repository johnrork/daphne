from django.db import models
# Stuff for sections
import markdown
from django.utils.safestring import mark_safe

# A handy shortcut for null & blank fields
nb = {'null': True, 'blank': True}


class Page(models.Model):
    title = models.CharField(max_length=50)
    slug  = models.SlugField()
    template = models.ForeignKey('Template')


class Section(models.Model):
    page  = models.ForeignKey(Page)
    type  = models.CharField(max_length=50)
    related_id = models.IntegerField()
    order = models.IntegerField()
    classes = models.CharField(max_length=100, **nb)

    def __unicode__(self):
        return self.type + ' section '+str(self.related_id)+', position '+str(self.order)+' on page '+str(self.page.id)

    def ident(self):
        return self.type+str(self.related_id)


class SectionModel(models.Model):
    section  = models.ForeignKey(Section)
    class Meta:
        abstract = True

    def get_content(self):
        return 'implement get_content on your model class'

    def ident(self):
        return self.type+str(self.id)


class TextImageSection(SectionModel):
    type  = 'TextImageSection'
    text  = models.TextField(**nb)
    image = models.ImageField(**nb)

    def get_content(self):
        return mark_safe(markdown.markdown(self.text))


class GallerySection(SectionModel):
    type = 'GallerySection'
    pass


class Template(models.Model):
    name = models.CharField(max_length=50)
    file = models.CharField(max_length=50)
    path = models.CharField(max_length=50, **nb)
