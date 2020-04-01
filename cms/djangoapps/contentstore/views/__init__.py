from os.path import join
from django.conf import settings
__path__.append(join(settings.CMS_ROOT, "djangoapps/contentstore/views"))

# pylint: disable=wildcard-import

"All view functions for contentstore, broken out into submodules"

# Disable warnings about import from wildcard
# All files below declare exports with __all__
from edx_platform.cms.djangoapps.contentstore.views.assets import *
from .component import *
from .course import *
from edx_platform.cms.djangoapps.contentstore.views.checklists import *
from edx_platform.cms.djangoapps.contentstore.views.entrance_exam import *
from edx_platform.cms.djangoapps.contentstore.views.error import *
from edx_platform.cms.djangoapps.contentstore.views.helpers import *
from edx_platform.cms.djangoapps.contentstore.views.item import *
from edx_platform.cms.djangoapps.contentstore.views.import_export import *
from edx_platform.cms.djangoapps.contentstore.views.library import *
from edx_platform.cms.djangoapps.contentstore.views.preview import *
from edx_platform.cms.djangoapps.contentstore.views.public import *
from edx_platform.cms.djangoapps.contentstore.views.export_git import *
from edx_platform.cms.djangoapps.contentstore.views.user import *
from edx_platform.cms.djangoapps.contentstore.views.tabs import *
from .videos import *
from edx_platform.cms.djangoapps.contentstore.views.transcript_settings import *
from edx_platform.cms.djangoapps.contentstore.views.transcripts_ajax import *
try:
    from edx_platform.cms.djangoapps.contentstore.views.dev import *
except ImportError:
    pass
