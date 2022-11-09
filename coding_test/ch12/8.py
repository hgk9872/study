# 문자열 재정렬 (p322)

data = input()

alpha = ""
number = 0

for x in data:
    if ord(x) >= ord("A"):
        alpha += x
    else:
        number += int(x)

s1 = sorted(alpha)

result = ""

for i in s1:
    result += i

print(result + str(number))