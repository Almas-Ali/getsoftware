from software.views import catagory
from django.contrib.sitemaps import Sitemap
from .models import Software, Catagory
from django.urls import reverse


class SoftwareSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Software.objects.all()

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return '/software/%s' % (obj.slug)


class CatagorySitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Catagory.objects.all()

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return '/catagory/%s' % (obj.slug)


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return ['software:index', 'software:contact', 'software:about', 'software:all_softwares']

    def location(self, item):
        return reverse(item)
