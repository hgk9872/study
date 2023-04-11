# https://www.acmicpc.net/problem/3986 s4

# 스택으로 빈 문자열 만들기
n = int(input())
count = 0

for _ in range(n):
    stack = []
    word = input()
    for i in range(len(word)):
        if stack:
            if stack[-1] == word[i]:
                stack.pop()
            else:
                stack.append(word[i])
        else:
            stack.append(word[i])
    
    if not stack:
        count += 1

print(count)