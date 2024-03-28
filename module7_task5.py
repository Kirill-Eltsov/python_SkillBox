from typing import Union, Callable
from operator import sub, mul, truediv, add
import logging
import logging.config

from Module7.module7_task1_2_utils import Numeric
from Module7.module7_task5_dict_config import dict_config

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

logging.config.dictConfig(dict_config)
logger = logging.getLogger('my_logger.utils')

def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    logger.info(f"Преобразование строкового символа: '{value}', в арифметический оператор")

    if not isinstance(value, str):
        logger.error("wrong operator type", value)
        raise ValueError("wrong operator type")
    if value not in OPERATORS:
        logger.error("wrong operator value", value)
        raise ValueError("wrong operator value")
    return OPERATORS[value]