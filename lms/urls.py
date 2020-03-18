from edx_platform.lms.urls import *
from edx_platform.lms.urls import urlpatterns
from django.conf.urls import include, url
from django.views.generic import TemplateView

robots = TemplateView.as_view(template_name='robots.txt', content_type='text/plain')
urlpatterns += [
    url(r'^robots\.txt$', robots, name='robots')
]
