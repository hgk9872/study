# 문자열 뒤집기

# 연속하는 문자열이 나올 때,
# 0, 1로 시작하는 연속문자열에서
# 첫 번째만 숫자를 세서 더 적은 숫자를 출력

s = input()

zero = 0
one = 0

if int(s[0]) == 0:
    zero += 1
else:
    one += 1

for i in range(len(s) - 1):
    diff = int(s[i + 1]) - int(s[i])
    if diff > 0:
        one += 1
    elif diff < 0:
        zero += 1

print(min(zero, one))