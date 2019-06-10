# f=float(input("请输入华氏温度"))
# c=(f-32)/1.8
# print("%.1f华氏温度 = %.1f摄氏度"% (f,c))


# import math
# radius = float(input("请输入圆周半径："))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print("周长：%.2f" % perimeter)
# print("面积：%.2f" % area)


year = int(input("请输入年份："))
is_leap = (year % 4 == 0 and year % 100 !=0 or year % 400 == 0)
print(is_leap)