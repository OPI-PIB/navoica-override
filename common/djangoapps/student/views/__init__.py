from os.path import join
from django.conf import settings
__path__.append(join(settings.COMMON_ROOT_EDX, 'djangoapps/student/view'))

from dashboard import *
from login import *
from management import *
