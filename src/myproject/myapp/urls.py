from django.conf.urls.defaults import patterns, url
from myapp.views import *

urlpatterns = patterns('myapp.views',
    url(r'^list$', mylist, name='list'),
)
