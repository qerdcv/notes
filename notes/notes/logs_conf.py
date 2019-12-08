import os
from .settings import BASE_DIR
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {

        },
    },
    'handlers': {
        'consumer': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'notes/logs/')+"debug.log",
            'formatter': 'verbose'
        },
    },

    'loggers': {
        'main.consumers': {
            'handlers': ['consumer'],
            'level': "INFO",
            'propagate': True,
        }
    }
}