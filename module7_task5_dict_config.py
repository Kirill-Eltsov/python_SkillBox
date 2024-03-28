dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "h",
            "interval": 10,
            "backupCount": 3,
            "level": "INFO",
            "formatter": "base",
            "filename": "utils.log",
        }
    },
    "loggers": {
        "module_logger": {
            "level": "DEBUG",
            "handlers": ["file", "console"],
        }
    }
}