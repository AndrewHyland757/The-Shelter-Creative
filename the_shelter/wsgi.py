#import os
#from django.core.wsgi import get_wsgi_application
#from whitenoise import WhiteNoise

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_shelter.settings')

#application = get_wsgi_application()
#application = WhiteNoise(application)


import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_shelter.settings')

application = get_wsgi_application()

# WhiteNoise static file serving with compression and caching
application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'staticfiles'))
application.add_files(os.path.join(os.path.dirname(__file__), 'static'), prefix='static/')
