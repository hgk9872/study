# https://www.acmicpc.net/problem/10988
# 브2
# reversed로 list 이용해서도 가능

word1 = input()

word2 = word1[::-1]

if word1 == word2:
    print(1)
else:
    print(0)