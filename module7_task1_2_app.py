#В этом файле сделаны задания 1, 2 и задание 3 с комментариями
import logging
from module7_task1_2_utils import string_to_operator
from module7_task3 import get_logger

#logger = get_logger('app') - Эта строчка для задания 3.
#Созданные файлы в задании 3 прилагаются calc_debug.log и calc_error.log
#Для задания 3 строчки 10-15 убираем и оставляем только строчку 6

logger = logging.getLogger('app')
logger.setLevel("INFO")
formatter = logging.Formatter("%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s")
console_handler = logging. StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def calc(args):
    #logger.debug(f"Arguments: {args}") - Эта строчка для задания 3
    logger.info(f"Arguments: {args}")

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]
    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.error("Error while converting number 1")
        logger.error(e)
    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.error("Error while converting number 1")
        logger.error(e)

    operator_func = string_to_operator(operator)
    result = operator_func(num_1, num_2)

    logger.info(f"Result {result}")
    logger.info(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    calc('2+3')
