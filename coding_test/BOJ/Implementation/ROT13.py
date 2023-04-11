# https://www.acmicpc.net/problem/11655 - 브1

data = input()

alpha1 = [x for x in range(ord('a'), ord('z') + 1)] # 소문자
alpha2 = [x for x in range(ord('A'), ord('Z') + 1)] # 대문자

for i in range(len(data)):
    x = ord(data[i])
    if x in alpha1: # 소문자
        idx = alpha1.index(x)
        rot_idx = (idx + 13) % 26
        print(chr(alpha1[rot_idx]), end = '')
    elif x in alpha2: # 대문자
        idx = alpha2.index(x)
        rot_idx = (idx + 13) % 26
        print(chr(alpha2[rot_idx]), end ='')
    else: # 공백 or 숫자
        print(data[i], end='')