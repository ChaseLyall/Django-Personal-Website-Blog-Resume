from django.conf.urls import patterns, include, url
from django.contrib import admin

from resume import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^resume/', views.resume, name='resume'),
)
