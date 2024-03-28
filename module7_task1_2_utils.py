#В этом файле сделаны задания 1, 2 и задание 3 с комментариями
from typing import Union, Callable
from operator import sub, mul, truediv, add
import logging
from module7_task3 import get_logger

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

#logger = get_logger('utils') - Эта строчка для задания 3
#Созданные файлы в задании 3 прилагаются calc_debug.log и calc_error.log
#Для задания 3 строчки 18-23 убираем и оставляем только строчку 13
Numeric = Union[int, float]

logger = logging.getLogger('utils')
logger.setLevel("ERROR")
formatter = logging.Formatter("%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    if not isinstance(value, str):
        logger.error("wrong operator type", value)
        raise ValueError("wrong operator type")
    if value not in OPERATORS:
        logger.error("wrong operator value", value)
        raise ValueError("wrong operator value")
    return OPERATORS[value]
