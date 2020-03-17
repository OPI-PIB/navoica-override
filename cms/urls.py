print('override')
from edx_platform.cms.urls import *
from edx_platform.cms.urls import urlpatterns
from django.conf import settings
from django.conf.urls import include, url
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from machina.app import board

urlpatterns += [url(r'^forum/', include(board.urls)),]

robots = TemplateView.as_view(template_name='robots.txt', content_type='text/plain')
urlpatterns += [
    url(r'^robots\.txt$', robots, name='robots')
]

# Favicon
favicon_path = configuration_helpers.get_value('favicon_path', settings.FAVICON_PATH)  # pylint: disable=invalid-name
urlpatterns += [
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + favicon_path, permanent=True)),
]
import sys
print('||||||||||||||||||||||||||')
print(sys.path)
