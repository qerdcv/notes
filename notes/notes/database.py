DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'notes',
        'USER': 'notes',
        'PASSWORD': 'notes',
        'HOST': 'notes_database',
        'PORT': '5432',
    }
}
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xcmez6j)*4_*7)7f#z!4!*3&gm@zmtpaxw$m0b&-_se3gl@pd-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
