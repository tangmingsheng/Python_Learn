for number1 in range(1,21):
    print(number1)

number2 = list(range(1,1000001))
for number_2 in number2:
    print(number_2)

number3 = min(number2)
print(number3)
number3 = max(number2)
print(number3)

number4 = list(range(1,21,2))
for number_4 in number4:
    print(number_4)

number5 = list(range(3, 31, 3))
for number_5 in number5:
    print(number_5)

number6 = [number_6**3 for number_6 in range(1,11)]
print(number6)