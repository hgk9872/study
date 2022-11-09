# https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3

s = "abababaabb"

answer = len(s)
result = ""
count = 1
for i in range(1, len(s) // 2):
    part = s[0:i]
    for j in range(i, len(s) - i, i):
        if part == s[j:j+i]:
            count += 1
        else:
            if count == 1:
                result += part
            else:
                result += str(count) + part
    count = 1
    result += s[j:j+i]
    print(result)
    result = ""