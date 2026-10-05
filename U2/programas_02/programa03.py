for num in range(11):
    if num % 2 == 0 and num != 0:
        print(num)

for num2 in range(11):
    if num2 % 2 != 0 or num == 0:
        continue
    print(num2)

num3 = 0
while num3 <= 10:
    print(num3)
    num3 += 2


num4 = 0
while num4 <= 10:
    if num4 != 0:
        num4 += 1
        continue
    print(num4)
    num4 += 1
