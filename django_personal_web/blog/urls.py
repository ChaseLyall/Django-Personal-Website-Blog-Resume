from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views, feed

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^blog/', views.BlogIndex.as_view(), name='blog_index'),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)
