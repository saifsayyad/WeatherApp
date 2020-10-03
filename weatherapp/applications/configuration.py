import sys
import os

APP_NAME = "weatherapp_app"
APP_DESCRIPTION = "groundwork application of package WeatherApp"
APP_PATH = os.path.join(os.path.expanduser('~'), "WeatherApp")

PLUGINS = ["YahooApiPlugin", "GwPluginsInfo", "GwWeb", "GwWebManager"]

YAHOO_APP_ID = "rMtISigh"
YAHOO_END_POINT = "https://weather-ydn-yql.media.yahoo.com/forecastrss"
CLIENT_ID = "dj0yJmk9THIyMmNEb1RScGRjJmQ9WVdrOWNrMTBTVk5wWjJnbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTRk"
CLIENT_SECRET = "9667eb91e98731b510c93f168d11afaf0d8c3b93"

GROUNDWORK_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "%(asctime)s - %(levelname)-5s - %(message)s"
        },
        'debug': {
            'format': "%(asctime)s - %(levelname)-5s - %(name)-40s - %(message)-80s - %(module)s:%("
                      "funcName)s(%(lineno)s)"
        },
    },
    'handlers': {
        'console_stdout': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'level': 'DEBUG'
        },
        'file': {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "debug",
            "filename": os.path.join(APP_PATH, "weatherapp.log"),
            "maxBytes": 1024000,
            "backupCount": 3,
            'level': 'DEBUG'
        },
        # 'file_my_plugin': {
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "formatter": "debug",
        #     "filename": "logs/my_plugin.log",
        #     "maxBytes": 1024000,
        #     "backupCount": 3,
        #     'level': 'DEBUG'
        # },
    },
    'loggers': {
        '': {
            'handlers': ['console_stdout'],
            'level': 'DEBUG',
            'propagate': False
        },
        'groundwork': {
            'handlers': ['console_stdout', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
        # 'MyPlugin': {
        #     'handlers': ['console_stdout', 'file_my_plugin'],
        #     'level': 'DEBUG',
        #     'propagate': False
        # },
    }
}
