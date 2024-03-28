import logging


class ASCIIFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if record.msg.isascii():
            return True
        else:
            return False


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s"
        }
    },
    'filters': {
            'ascii_filter': {
                '()': ASCIIFilter,
            }
        },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filters": ['ascii_filter', ],
        }
    },
    "loggers": {
        "module_logger": {
            "level": "DEBUG",
            "handlers": ["console"],
        }
    }
}

