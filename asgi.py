"""
ASGI config for data_analysis_project project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_analysis_project.settings')

application = get_asgi_application()