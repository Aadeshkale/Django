Creating model in django
1.setup database configration in settings.py file

example,
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample',
        'USER': 'root',
        'PASSWORD': 'dx619',
    }
}


2.check database connection

from django.db import connection
c=connection.cursor()
