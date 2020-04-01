from os.path import join
from django.conf import settings
__path__.append('/edx/app/edxapp/edx-platform/edx_platform/lms/djangoapps/certificates/views')

from edx_platform.lms.djangoapps.certificates.views.xqueue import *
from edx_platform.lms.djangoapps.certificates.views.support import *
from .webview import *
