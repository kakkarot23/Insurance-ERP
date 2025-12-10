"""
ASGI config for insurance_erp project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insurance_erp.settings')

application = get_asgi_application()
