import json
import logging

class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        new_message = json.dumps(msg, ensure_ascii=False)
        return new_message, kwargs

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("skillbox_json_messages.log.json")
    formatter = logging.Formatter('{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}', datefmt="%H:%M:%S")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger = JsonAdapter(logger, {})

    logger.info('Сообщение')
    logger.error('Кавычка)"')
    logger.debug("Еще одно сообщение")
