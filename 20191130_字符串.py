import sys


# a, b = 5, 10
# print('%d * %d = %d' % (a, b, a * b))
#
# list1 = ['orange', 'apple', 'zoo', 'straberry', 'blueberry']
# list2 = sorted(list1)
# list3 = sorted(list1, reverse=True)
# list4 = sorted(list1, key=len)
#
# print(list1)
# print(list2)
# print(list3)
# print(list4)
#
# list1.sort(reverse=True)
#
# print(list1)
#
# f = [x for x in range(1, 10)]
# print(f)
#
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
#
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))
# print(f)
#
# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))
# print(f)
# for val in f:
#     print(val)

# 在屏幕上显示跑马灯文字。
# import os
# import time
#
# def main():
#     content = '北京欢迎你，为你开天辟地……'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#
# if __name__ == '__main__':
#        main()

# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

# import random
#
# def generate_code(code_len=4):
#     allcharts = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#     last_pos = len(allcharts) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += allcharts[index]
#     # print(code)
#     return code
#
#  # if __name__ == '__generate_code__':
# print(generate_code(10))

# scores = {'tang': 95, 'mings': 84, 'sheng': 73}
# print(scores)
#
# item1 = dict(one=1, two=2, three=3, four=4)
# item2 = dict(zip(['a', 'b', 'c'], '123'))
# item3 = {num: num ** 2 for num in range(1, 10)}
#
# print(item1)
# print(item2)
# print(item3)
# print(item1, item2, item3)
#
# print(scores['tang'])
# print(item2['a'])
# print(item3['9'])

# 计算指定的年月日是这一年的第几天。
def if_leaf_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, day):
    days_of_month=[[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][if_leaf_year(year)]
    # days_of_month[]=days_of_month1[if_leaf_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + day


def main():
    print(which_day(1992,2,11))
    print(which_day(1993,7,25))


if __name__ == '__main__':
    main()
