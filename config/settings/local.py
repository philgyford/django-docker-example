"""
Settings used for local development.
"""

from .base import *


DEBUG = True


# Debug Toolbar settings.
if DEBUG:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    # 10.0.2.2 is what we need when using Vagrant:
    # INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', '0.0.0.0',]

    # Stop Django handling static files in favour of Whitenoise.
    # (When DEBUG = False)
    # Need to add the app just before staticfiles, so:
    # new_apps = []
    # for app in INSTALLED_APPS:
    #     if app == 'django.contrib.staticfiles':
    #         new_apps.append('whitenoise.runserver_nostatic')
    #     new_apps.append(app)
    # INSTALLED_APPS[:] = new_apps

    def show_toolbar(request):
        if request.is_ajax():
            return False
        return True

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': 'config.settings.local.show_toolbar',
    }
