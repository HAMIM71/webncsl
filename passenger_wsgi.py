import sys
import os

# Add your project root to the Python path
sys.path.insert(0, '/home4//webncsl')  # <-- replace 'username' with your Bluehost username

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'webncsl.settings'

# Import Django WSGI application
from webncsl.wsgi import application
