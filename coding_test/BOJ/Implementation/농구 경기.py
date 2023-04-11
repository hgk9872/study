# https://www.acmicpc.net/problem/1159
# 브2

n = int(input())

alpha = [0] * 26

for _ in range(n):
    s = input()
    idx = ord(s[0]) - ord('a')
    alpha[idx] += 1

answer = ''

for i in range(26):
    if alpha[i] >= 5:
        answer += chr(i + ord('a'))

if answer:
    print(answer)
else: # 빈 문자열
    print('PREDAJA')
