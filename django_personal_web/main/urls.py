from django.conf.urls import patterns, include, url
from django.contrib import admin


from main import views as views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^', include('resume.urls')),
    url(r'^', include('blog.urls')),
)
