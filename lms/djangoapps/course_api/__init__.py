from os.path import join
from django.conf import settings
from openedx.core.djangoapps.waffle_utils import (WaffleSwitch, WaffleSwitchNamespace)

__path__.append('/edx/app/edxapp/edx-platform/edx_platform/lms/djangoapps/course_api')
WAFFLE_SWITCH_NAMESPACE = WaffleSwitchNamespace(name='course_list_api_rate_limit')

USE_RATE_LIMIT_2_FOR_COURSE_LIST_API = WaffleSwitch(WAFFLE_SWITCH_NAMESPACE, 'rate_limit_2')
USE_RATE_LIMIT_10_FOR_COURSE_LIST_API = WaffleSwitch(WAFFLE_SWITCH_NAMESPACE, 'rate_limit_10')
