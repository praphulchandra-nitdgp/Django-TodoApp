import os
import sys
import site

# Add the project directory to the sys.path
sys.path.insert(0, '/home/praphulchandraganapathri/todo_django')

# Add the virtual environment site-packages to the sys.path
site.addsitedir('/home/praphulchandraganapathri/todo_django/virtualenv/lib/python3.10/site-packages')

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_django.settings')

# Import and setup the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

