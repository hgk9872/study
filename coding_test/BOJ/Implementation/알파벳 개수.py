# https://www.acmicpc.net/problem/10808
# 브4

word = input()
alpha = [0] * 26

for i in range(len(word)):
    idx = ord(word[i])-ord('a')
    alpha[idx] += 1

print(*alpha)