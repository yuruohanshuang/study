# 格式化前 ❌
import os

import requests

from src.utils import get_logger


def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
