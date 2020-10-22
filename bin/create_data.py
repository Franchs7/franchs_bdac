#!/usr/bin/python
import os
import string
import sys
import random
import time


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bdac.settings')
# try:
#     from django.core.management import execute_from_command_line
# except ImportError as exc:
#     raise ImportError(
#         "Couldn't import Django. Are you sure it's installed and "
#         "available on your PYTHONPATH environment variable? Did you "
#         "forget to activate a virtual environment?"
#     ) from exc
# execute_from_command_line(sys.argv)


def create_dbname():
    res = ''.join(random.sample(string.ascii_letters, 5))
    return res


def create_tablename():
    res = ''.join(random.sample(string.ascii_letters, 8))
    return res


def create_time():
    a1 = (2020, 6, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
    a2 = (2020, 9, 30, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（1990-12-31 23：59：59）
    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳
    # 随机生成10个日期字符串
    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
    return date


def one_data():
    dbname = create_dbname()
    tablename = create_tablename()
    time = create_time()
    return '{}\t{}\t{}\n'.format(dbname, tablename, time)


if __name__ == '__main__':
    with open('data.txt', 'w') as f:
        for i in range(200000):
            res = one_data()
            f.write(res)

    a = {'a':1, 'b':2, 'c':3, 'd':4}
