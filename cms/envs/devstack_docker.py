""" Overrides for Docker-based devstack. """

from .devstack import *  # pylint: disable=wildcard-import, unused-wildcard-import

# Docker does not support the syslog socket at /dev/log. Rely on the console.
LOGGING['handlers']['local'] = LOGGING['handlers']['tracking'] = {
    'class': 'logging.NullHandler',
}

LOGGING['loggers']['tracking']['handlers'] = ['console']

LMS_BASE = os.environ.get('LMS_BASE', '10.10.32.151:18000')
CMS_BASE = os.environ.get('CMS_BASE', '10.10.32.151:18010')

LMS_ROOT_URL = 'http://{}'.format(LMS_BASE)

FEATURES.update({
    'ENABLE_COURSEWARE_INDEX': True,
    'ENABLE_LIBRARY_INDEX': True,
    'ENABLE_DISCUSSION_SERVICE': True,
    'ENABLE_CREATOR_GROUP': True,
})

CREDENTIALS_SERVICE_USERNAME = 'credentials_worker'

OAUTH_OIDC_ISSUER = '{}/oauth2'.format(LMS_ROOT_URL)

JWT_AUTH.update({
    'JWT_SECRET_KEY': 'lms-secret',
    'JWT_ISSUER': OAUTH_OIDC_ISSUER,
    'JWT_AUDIENCE': 'lms-key',
})
TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'pl'

DEFAULT_FROM_EMAIL = 'registration@'+LMS_BASE
DEFAULT_FEEDBACK_EMAIL = 'feedback@'+LMS_BASE
SERVER_EMAIL = 'devops@'+LMS_BASE

SETTINGS_EXPORT = [
    'PLATFORM_NAME',
    'LMS_ROOT_URL',
    'STUDIO_NAME',
    'FAVICON_PATH',
]

from .common import _make_mako_template_dirs

SITE_ID = 1
# dir containing all themes
COMPREHENSIVE_THEME_DIRS = [REPO_ROOT_OVERRIDE / "themes"]
# Theme directory locale paths
COMPREHENSIVE_THEME_LOCALE_PATHS = []
# Theme to use when no site or site theme is defined,
# set to None if you want to use openedx theme
DEFAULT_SITE_THEME = 'navoica-theme'

ENABLE_COMPREHENSIVE_THEMING = True

TEMPLATES[1]["DIRS"] = _make_mako_template_dirs
derive_settings(__name__)
