from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView

from software import views
from .sitemaps import CatagorySitemap, SoftwareSitemap, StaticSitemap

app_name = "software"
handler404 = 'software.views.handler404'

sitemaps = {
    'software': SoftwareSitemap,
    'catagory': CatagorySitemap,
    'static': StaticSitemap,
}


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register, name='register'),
    path('search', views.userSearch, name='search'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('download', views.download, name='download'),
    path('catagory', views.catagory, name='catagory'),
    path('catagory/<str:slug>', views.sub_catagory, name='sub_catagory'),
    path('software', views.all_softwares, name='all_softwares'),
    path('software/<str:slug>', views.softwares, name='softwares'),
    path('profile', views.profile, name='profile'),
    path('like/id=<str:id>/post_id=<str:post_id>', views.like, name='like'),
    path('comment/post_id=<str:post_id>', views.comment, name='comment'),
    path('404', views.handler404, name='handler404'),
    path('auto-suggest', views.auto_suggest, name='auto_suggest'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(
        template_name='robots.txt', content_type='text/plain')),
]
