import logging
import logging.config

class LevelFileHandler(logging.Handler):
    def __init__(self, filename, mode='a'):
        super().__init__()
        self.filename = filename
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        if record.levelname == "DEBUG":
            self.filename = "calc_debug.log"
        elif record.levelname == "ERROR":
            self. filename = "calc_error.log"
        with open(self.filename, mode=self.mode) as file:
            file.write(message + '\n')


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
            "()": LevelFileHandler,
            "level": "DEBUG",
            "formatter": "base",
            "filename": "logger.log",
            "mode": "a",
        }
    },
    "loggers": {
        "module_logger": {
            "level": "DEBUG",
            "handlers": ["file", "console"],
        }
    }
}


def get_logger(name):
    logging.config.dictConfig(dict_config)
    logger = logging.getLogger(f"module_logger. {name}")
    return logger
