# 格式化前 ❌
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s", datefmt="")


def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def divide(a, b):
    return a / b


list1 = [(10, 2), (8, 0), (6, 3)]
count = 0
for a in list1:
    try:
        divide(a[0], a[1])
        count = count + 1
    except ZeroDivisionError:
        logging.error("除零错误: %s / %s", a[0], a[1])
    except Exception as e:
        logging.error("发生错误: %s", e)

print(count)
