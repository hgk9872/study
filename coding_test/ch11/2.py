# 곱하기 혹은 더하기 (p.312)

s = input()

total = int(s[0])

for i in range(1, len(s)):
    if total <= 1 or int(s[i]) <= 1:
        total += int(s[i])
    else:
        total *= int(s[i])

print(total)