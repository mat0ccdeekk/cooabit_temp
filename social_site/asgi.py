"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_site.settings")
django.setup()
application = get_default_application()


from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
