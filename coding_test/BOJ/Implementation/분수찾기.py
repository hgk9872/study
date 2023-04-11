# https://www.acmicpc.net/problem/1193 실5

# line 짝수, 홀수 구분
# 1 + 2 + 3 + 4 + ...

x = int(input())

line = 1
count = 1

# x = 5일 때..
while x > count:
    line += 1
    count += line

diff = count - x
a = line - diff
b = 1 + diff
if line % 2 == 1: # 홀수일 때
    print(f'{b}/{a}')
else:
    print(f'{a}/{b}')
