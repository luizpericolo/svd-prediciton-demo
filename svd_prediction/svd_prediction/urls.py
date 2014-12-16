from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import home, prediction_result

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'svd_prediction.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home),
    url(r'^result/', prediction_result),
)
