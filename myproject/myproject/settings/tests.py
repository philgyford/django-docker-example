"""
Settings used for running tests.
"""

from .base import *


CACHES = {
    'default': {
        # Use dummy cache (ie, no caching):
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
